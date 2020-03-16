<template>
  <div >
    <!-- EDITION COMPONENT -->
      <b-button lg="4" variant="outline-primary" @click="Edition">Editar</b-button>


    <!-- EDITION COMPONENT -->
  </div>
</template>
<script>
export default {
  name: "EditionButton",
  methods: {
    Edition(item) {
      this.$emit('clicked-edition', item)
    }
  }
};
</script>
<style lang="stylus"></style>