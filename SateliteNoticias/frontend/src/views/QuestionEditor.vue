<template>
    <div class="container mt-2">
        <h1 class="mb-3">Ask a question</h1>
        <form @submit.prevent="onSubmit">

            <textarea v-model= "question_body"
            class= "form-control"
            placeholder="What do you want to ask"
            rows="3">

            <br>
            </textarea>
                <button type= "submit" class=" mt-4 btn btn-success"> Publish</button>

        </form>
        <p v-if="error" class="muted mt-2"> {{error}}</p>
    </div>
</template>

<script>
import { apiService } from '../common/api.service'
export default {
    name:"QuestionEditor",
    data (){
        return {
            question_body: null,
            error: null
        }
    },
    methods: {
        onSubmit() {
            if (!this.question_body){
                this.error = "You cant send an empty question!"
            }
            else if (this.question_body.length > 240) {
                this.error ="ENsure this field has no more than 240 characters!"
                
            }
            else {
                let endpoint = "/api/questions/"
                let method = "POST";
                apiService(endpoint, method, {content: this.question_body})
                    .then(question_data => {
                        this.$router.push({ 
                            name: 'question', 
                            params: { slug: question_data.slug } 
                        })
                    })
            }
        }
    },
    created(){
        document.title = "Editor - Satelite de Noticias"
    }
    
}
</script>
