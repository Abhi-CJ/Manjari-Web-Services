const CACHE_NAME = 'manjari-taxi-v1';
const urlsToCache = [
    '/',
    '/static/css/style.min.css',
    '/static/js/main.min.js'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(urlsToCache).catch(() => {
                console.log('Some assets could not be cached during install');
            });
        })
    );
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

self.addEventListener('fetch', event => {
    const { request } = event;
    const url = new URL(request.url);

    if (request.method !== 'GET') {
        return;
    }

    if (url.pathname.match(/\.(js|css|png|jpg|jpeg|gif|svg|webp|woff|woff2)$/)) {
        event.respondWith(
            caches.match(request).then(response => {
                return response || fetch(request).then(response => {
                    if (response && response.status === 200) {
                        const responseClone = response.clone();
                        caches.open(CACHE_NAME).then(cache => {
                            cache.put(request, responseClone);
                        });
                    }
                    return response;
                }).catch(() => {
                    return caches.match(request);
                });
            })
        );
    }
    else if (request.headers.get('accept').includes('text/html')) {
        event.respondWith(
            fetch(request).then(response => {
                if (response && response.status === 200) {
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then(cache => {
                        cache.put(request, responseClone);
                    });
                }
                return response;
            }).catch(() => {
                return caches.match(request);
            })
        );
    }
});
