self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open('myshop-cache').then((cache) => {
            return cache.addAll([
                '/',
                '/cart/',
                '/checkout/',
            ]);
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
