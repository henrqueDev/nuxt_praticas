import { conversorStore } from '~/stores/conversor/conversor';

export default defineNuxtPlugin(({ $pinia }) => {
  return {
    provide: {
      conversorStore: conversorStore($pinia)
    }
  }
})