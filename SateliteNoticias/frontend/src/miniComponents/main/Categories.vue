<template>
  <b-col md="2">
    <div class="dropdown p-4">
      <md-menu md-size="big" md-align-trigger>
        <md-button md-menu-trigger class="md-raised md-primary"
          >CATEGORIAS</md-button
        >

        <md-menu-content>
          <md-menu-item
            v-for="axis in Axis"
            :key="axis.key"
            @click="categoryClicked(axis)"
          >
            {{ axis }}
          </md-menu-item>
        </md-menu-content>
      </md-menu>
    </div>
  </b-col>
</template>
<script>
export default {
  name: "Categories",
  data() {
    return {
      Axis: [
        "Big Data",
        "Pagos Digitales",
        "CBCD",
        "Criptoactivos",
        "Banca abierta",
        "Ciberseguridad",
        "Monitoreo tecnologico",
        "DLT"
      ]
    };
  },
  methods: {
    categoryClicked(item) {
      this.$emit("clicked-category", item);
    }
  }
};
</script>
<style scoped></style>
