<template>
  <div style="text-align:center">
    <h2 style="color: blue">{{ title }}</h2>
    <div style="padding: 7px"></div>
    <div
      style="color: blue;border:1px solid blue;font-size: 15px;text-align:center "
    >
      <a>{{ link }}</a>

      <!--TODO: DISABLE DEL SCROLL DE LAS NOTICIAS PARA PODER SCROLLEAR EL CONTENIDO SIN PROBLEMAS 
                        CONDICIONES: ESTAR EN HOVER EN EL ELEMENTO
              -->
      <vue-custom-scrollbar
        class="scroll-area"
        v-bind:style="{
          position: 'relative',
          margin: 'auto',

          width: '100%',
          height: '25em'
        }"
        :settings="settings"
      >
        <div style="padding:3em"></div>

        <p v-html="content"></p>
      </vue-custom-scrollbar>

      <div style="padding-top: 1em"></div>

      <b-row>
        <b-col>
          <router-link
            :to="{
              name: 'news-fullEditor',
              params: {
                slug: this.slug,
                fullContent: this.fullContent,
                newsPiece: this.newsPiece
              }
            }"
            class="btn btn-sm btn-outline-secondary mr-1"
            >Seguir leyendo
          </router-link>
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
        <h6 class="text-primary text-right" style="padding:10px">
          #Visitas: 200
        </h6>
      </div>
    </div>
  </div>
</template>
<script>
import vueCustomScrollbar from "vue-custom-scrollbar";

export default {
  name: "NewsSummary",
  props: {
    openOrClosed: Boolean,
    title: String,
    content: String,
    link: String,
    slug: String,
    fullContent: String,
    newsPiece: Object
  },
  data() {
    return {
      settings: {
        maxScrollbarLength: 20
      },
      reading: "Seguir leyendo"
    };
  },
  components: {
    vueCustomScrollbar
  },
  created() {
  },
  methods: {}
};
</script>
<style scoped></style>
