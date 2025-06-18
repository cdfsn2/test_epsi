package com.simplecity.amp_library.exceptions;

public class AppExceptions {
    public static class DatabaseException extends RuntimeException {
        public DatabaseException(String message) {
            super(message);
        }

        public DatabaseException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    public static class MediaPlayerException extends RuntimeException {
        public MediaPlayerException(String message) {
            super(message);
        }

        public MediaPlayerException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    public static class NotificationException extends RuntimeException {
        public NotificationException(String message) {
            super(message);
        }

        public NotificationException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    public static class ArtworkException extends RuntimeException {
        public ArtworkException(String message) {
            super(message);
        }

        public ArtworkException(String message, Throwable cause) {
            super(message, cause);
        }
    }
} 