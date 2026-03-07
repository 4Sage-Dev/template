import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: './player.html'
      }
    }
  },
  server: {
    port: 5174,
    open: '/player.html'
  }
});
