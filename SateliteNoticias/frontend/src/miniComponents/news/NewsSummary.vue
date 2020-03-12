<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <b-jumbotron
          bg-variant="white"
          header="Titulo Noticias"
          text-variant="primary"
          border-variant="primary"
          lead="Link:www.páginawb.cl"
        >
          <p>Resumen Noticias</p>
          <b-button lg="4" variant="outline-primary" href="#">Seguir leyendo</b-button>
          <div>
            <b-dropdown
              split
              split-variant="outline-primary"
              variant="primary"
              text="Lista de editores"
              class="m-2"
            >
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here...</b-dropdown-item>
            </b-dropdown>
          </div>
        </b-jumbotron>
      </b-col>
    </b-row>

    <b-row>
      <b-col md="12" class="p-3">
        <h4 class="text-primary text-right">#Visitas=200</h4>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: "NewsSummary"
};
</script>
<style lang="stylus"></style>