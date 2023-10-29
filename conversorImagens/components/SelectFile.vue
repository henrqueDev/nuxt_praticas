<template>
    <div>
    
        <div class="mb-3">
            <label for="formFile" class="form-label"></label>
            <input @change="(event)=> setarFormData(event)" class="form-control" type="file" id="formFile">
        </div>

        <div>
            <button class="btn-primary" @click="chamada">Baixar</button>
        </div>

    </div>
</template>

<script lang="js">
    import { conversorStore } from '~/stores/conversor/conversor';
   export default { 
    data() {
    return {
        formData: new FormData()
    }
    },
    methods: {
        setarFormData(e) {
            const files = e.target.files;
            this.formData = new FormData();
            this.formData.append('file', files[0]);
            console.log(this.formData)
        },
        async chamada() {
            const a = await conversorStore().useApi( this.formData )
            console.log(a)
            return a
        }
    }
   }
</script>