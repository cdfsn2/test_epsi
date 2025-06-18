package com.simplecity.amp_library.model;

public class UserSelectedArtwork {

    @ArtworkProvider.Type
    private int type;
    private String path;

    public UserSelectedArtwork(@ArtworkProvider.Type int type, String path) {
        this.type = type;
        this.path = path;
    }

    @ArtworkProvider.Type
    public int getType() {
        return type;
    }

    public void setType(@ArtworkProvider.Type int type) {
        this.type = type;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    @Override
    public String toString() {
        return "UserSelectedArtwork{" +
                "type=" + type +
                ", path='" + path + '\'' +
                '}';
    }
}
