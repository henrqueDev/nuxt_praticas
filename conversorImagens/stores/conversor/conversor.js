import { defineStore } from 'pinia';

export const conversorStore = defineStore('conversor', {
  actions: {
    async useApi( formdata ) {
    const { data: res } = await $fetch("http://127.0.0.1:5000/converterImagemPng", {
      method: 'post',
      body: formdata
    })
    return res
    }
  }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(conversorStore, import.meta.hot))
}
