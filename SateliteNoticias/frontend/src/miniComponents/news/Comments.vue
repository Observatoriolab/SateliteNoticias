<template>
    <div style="border:1px solid blue; padding:0.8em 0.8em 0.8em 0.8em ">
        <div>
        <h4 class="text-primary p-2">Comentarios</h4>

              <b-form-textarea
                      id="textarea"
                      placeholder="Escribe tu comentario aqui!"
                      rows="3"
                      max-rows="12"
                    ></b-form-textarea>

        </div>

          <div style="padding: 1em"></div>
        <vue-custom-scrollbar class="scroll-area" v-bind:style="{position: 'relative',
                                                          margin: 'auto',
                                                          
                                                          width: '100%',
                                                          height: '20em' }"
                                                      :settings="settings" 
                                                     >


                        <ul class="list-unstyled">
                          <b-media tag="li">
                            <template v-slot:aside>
                              <b-img blank blank-color="#abc" width="64" alt="placeholder"></b-img>
                            </template>
                            <h5 class="mt-0 mb-1">List-based media object</h5>
                            <p class="mb-0">
                              Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                              Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                              ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                            </p>
                          </b-media>

                          <b-media tag="li" class="my-4">
                            <template v-slot:aside>
                            <b-img blank blank-color="#cba" width="64" alt="placeholder"></b-img>
                            </template>

                            <h5 class="mt-0 mb-1">List-based media object</h5>
                            <p class="mb-0">
                              Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                              Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                              ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                            </p>
                          </b-media>

                          <b-media tag="li">
                            <template v-slot:aside>
                              <b-img blank blank-color="#bac" width="64" alt="placeholder"></b-img>
                            </template>

                            <h5 class="mt-0 mb-1">List-based media object</h5>
                            <p class="mb-0">
                              Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                              Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                              ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                            </p>
                          </b-media>
                            <b-media tag="li">
                            <template v-slot:aside>
                              <b-img blank blank-color="#bac" width="64" alt="placeholder"></b-img>
                            </template>

                            <h5 class="mt-0 mb-1">List-based media object</h5>
                            <p class="mb-0">
                              Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                              Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                              ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                            </p>
                          </b-media>
                            <b-media tag="li">
                            <template v-slot:aside>
                              <b-img blank blank-color="#bac" width="64" alt="placeholder"></b-img>
                            </template>

                            <h5 class="mt-0 mb-1">List-based media object</h5>
                            <p class="mb-0">
                              Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                              Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                              ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                            </p>
                          </b-media>
                            <b-media tag="li">
                            <template v-slot:aside>
                              <b-img blank blank-color="#bac" width="64" alt="placeholder"></b-img>
                            </template>

                            <h5 class="mt-0 mb-1">List-based media object</h5>
                            <p class="mb-0">
                              Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                              Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                              ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                            </p>
                          </b-media>
                        </ul>

          </vue-custom-scrollbar>

</div>
</template>
<script>
import vueCustomScrollbar from 'vue-custom-scrollbar'

export default {
    name:"Comments",
     data() {
    return {
      settings: {
        maxScrollbarLength: 20
          }
        }
      },
      components: {
        vueCustomScrollbar

      },
}
</script>
<style scoped>

</style>