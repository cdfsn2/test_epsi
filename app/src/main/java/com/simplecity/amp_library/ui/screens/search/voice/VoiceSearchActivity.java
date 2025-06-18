package com.simplecity.amp_library.ui.screens.search.voice;

import android.app.SearchManager;
import android.content.ComponentName;
import android.content.Intent;
import android.os.Bundle;
import android.os.IBinder;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import com.annimon.stream.Stream;
import com.simplecity.amp_library.data.Repository;
import com.simplecity.amp_library.model.AlbumArtist;
import com.simplecity.amp_library.model.Song;
import com.simplecity.amp_library.playback.MediaManager;
import com.simplecity.amp_library.ui.common.BaseActivity;
import com.simplecity.amp_library.ui.screens.main.MainActivity;
import com.simplecity.amp_library.utils.ComparisonUtils;
import com.simplecity.amp_library.utils.LogUtils;
import com.simplecity.amp_library.utils.extensions.AlbumExtKt;
import dagger.android.AndroidInjection;
import io.reactivex.Observable;
import io.reactivex.Single;
import io.reactivex.android.schedulers.AndroidSchedulers;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import javax.inject.Inject;
import kotlin.Unit;
import kotlin.jvm.functions.Function1;

import static com.simplecity.amp_library.utils.StringUtils.containsIgnoreCase;

public class VoiceSearchActivity extends AppCompatActivity {

    private static final String TAG = "VoiceSearchActivity";

    private String filterString;

    private Intent intent;

    private int position = -1;

    @Inject
    MediaManager mediaManager;

    @Inject
    Repository.SongsRepository songsRepository;

    @Inject
    Repository.AlbumsRepository albumsRepository;

    @Inject
    Repository.AlbumArtistsRepository albumArtistsRepository;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        AndroidInjection.inject(this);
        super.onCreate(savedInstanceState);

        intent = getIntent();

        filterString = intent.getStringExtra(SearchManager.QUERY);
    }

    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
        super.onServiceConnected(name, service);
        if (intent != null && intent.getAction() != null && intent.getAction().equals("android.media.action.MEDIA_PLAY_FROM_SEARCH")) {
            searchAndPlaySongs();
        }
    }

    @Override
    public void onServiceDisconnected(ComponentName name) {
    }

    private Observable<List<Song>> getFilteredAlbumArtistSongs() {
        return albumArtistsRepository.getAlbumArtists()
                .first(Collections.emptyList())
                .flatMapObservable(Observable::fromIterable)
                .filter(this::matchesFilter)
                .flatMapSingle(albumArtist -> albumArtist.getSongsSingle(songsRepository))
                .map(this::sortSongs);
    }

    private boolean matchesFilter(AlbumArtist albumArtist) {
        return albumArtist.name.toLowerCase(Locale.getDefault())
                .contains(filterString.toLowerCase());
    }

    private List<Song> sortSongs(List<Song> songs) {
        Collections.sort(songs, (a, b) -> a.getAlbumArtist().compareTo(b.getAlbumArtist()));
        Collections.sort(songs, (a, b) -> a.getAlbum().compareTo(b.getAlbum()));
        Collections.sort(songs, (a, b) -> ComparisonUtils.compareInt(a.track, b.track));
        Collections.sort(songs, (a, b) -> ComparisonUtils.compareInt(a.discNumber, b.discNumber));
        return songs;
    }

    private void searchAndPlaySongs() {
        Observable.concat(
                getFilteredAlbumArtistSongs(),
                // Add other search sources here if needed
                Observable.empty()
        )
        .filter(songs -> !songs.isEmpty())
        .first(Collections.emptyList())
        .subscribe(
                songs -> {
                    if (!songs.isEmpty()) {
                        mediaManager.playAll(songs, position, true, () -> {
                            // Todo: Show playback error toast
                            return Unit.INSTANCE;
                        });
                        startActivity(new Intent(this, MainActivity.class));
                    }
                    finish();
                },
                error -> {
                    LogUtils.logException(TAG, "Error searching songs", error);
                    startActivity(new Intent(this, MainActivity.class));
                    finish();
                }
        );
    }

    @Override
    protected String screenName() {
        return TAG;
    }
}