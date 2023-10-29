import { defineNuxtConfig } from 'nuxt/config';

export default defineNuxtConfig({
  modules: ['@pinia/nuxt'],
  imports: {
    dirs: ['./stores'],
  },
  pinia: {
    autoImports: ['conversorStore', 'acceptHMRUpdate'],
  },
})