<template>
      <div style="text-align:center">
      
          <h2 style="color: blue">{{title}}</h2>
          <div style="padding: 7px"></div>
          <div style="color: blue;border:1px solid blue;font-size: 15px; ">
                    <a>{{link}}</a>


              <!--TODO: DISABLE DEL SCROLL DE LAS NOTICIAS PARA PODER SCROLLEAR EL CONTENIDO SIN PROBLEMAS 
                        CONDICIONES: ESTAR EN HOVER EN EL ELEMENTO
              -->

                     <vue-custom-scrollbar class="scroll-area" v-bind:style="{position: 'relative',
                                                          margin: 'auto',
                                                          
                                                          width: '100%',
                                                          height: '10em' }"
                                                      :settings="settings" 
                                                     >
                          <p >  {{content}}
                                     </p>
                    </vue-custom-scrollbar>

                            <div style="padding-top: 1em"></div>

                    <b-row>

                      <b-col>
                          <b-button @click="fullNewsClicked" lg="4" variant="outline-primary" ref="readingButton">{{reading}}</b-button>


                      </b-col>

                        <b-col>
                            <b-dropdown
                                  split
                                  split-variant="outline-primary"
                                  variant="primary"
                                  text="Lista de editores"
                                  class="m-1"
                                >
                                  <b-dropdown-item href="#">Action</b-dropdown-item>
                                  <b-dropdown-item href="#">Another action</b-dropdown-item>
                                  <b-dropdown-item href="#">Something else here...</b-dropdown-item>
                                </b-dropdown>
                        
                      </b-col>
                        
                  </b-row>

              <div style="border:1px solid blue">

                  <h6 class="text-primary text-right" style= "padding:10px">#Visitas: 200</h6>

              </div>
          </div>

      </div>
</template>
<script>
import vueCustomScrollbar from 'vue-custom-scrollbar'

export default {
  name: "NewsSummary",
  props:{
    openOrClosed: Boolean,
    title:String,
    content:String,
    link:String
  },
  data() {
    return {
      settings: {
        maxScrollbarLength: 20
      },
      reading: "Seguir leyendo"
    }
  },
  components: {
     vueCustomScrollbar

  },
  created(){
    console.log("aqui va algo")
    console.log(this.props)
  },
  methods:{
    fullNewsClicked() {
      if(this.openOrClosed){
        this.openOrClosed = false
      this.reading = "Seguir Leyendo"

      }
      else{
        this.openOrClosed = true
        this.reading = "Cerrar noticia"


      }
        this.$emit('clicked-fullNews', this.openOrClosed)    
    }
  }
};
</script>
<style scoped>

</style>