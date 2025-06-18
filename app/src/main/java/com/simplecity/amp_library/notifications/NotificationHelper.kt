package com.simplecity.amp_library.notifications

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build
import com.simplecity.amp_library.exceptions.AppExceptions.NotificationException
import com.simplecity.amp_library.utils.LogUtils

class NotificationHelper(private val context: Context) {

    private val notificationManager: NotificationManager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager

    fun createNotificationChannel(channelId: String, channelName: String, importance: Int) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            try {
                val channel = NotificationChannel(channelId, channelName, importance)
                notificationManager.createNotificationChannel(channel)
            } catch (e: Exception) {
                LogUtils.logException(TAG, "Failed to create notification channel", e)
                throw NotificationException("Failed to create notification channel", e)
            }
        }
    }

    fun showNotification(notificationId: Int, notification: Notification) {
        try {
            notificationManager.notify(notificationId, notification)
        } catch (e: Exception) {
            LogUtils.logException(TAG, "Failed to show notification", e)
            throw NotificationException("Failed to show notification", e)
        }
    }

    companion object {
        private const val TAG = "NotificationHelper"
    }
} 