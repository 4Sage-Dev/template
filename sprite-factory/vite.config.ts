import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: './gallery.html'
      }
    }
  },
  server: {
    open: '/gallery.html'
  }
});
