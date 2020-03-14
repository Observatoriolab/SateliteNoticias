<template>
  <b-col md="2">
    <div class="dropdown p-4">
     <md-menu md-size="big"  md-align-trigger>
      <md-button md-menu-trigger  class="md-raised md-primary">CATEGORIAS</md-button>

      <md-menu-content>
        <md-menu-item  @click="categoryClicked('My Item 1')">My Item 1</md-menu-item>
        <md-menu-item>My Item 2</md-menu-item>
        <md-menu-item>My Item 3</md-menu-item>

        <md-menu-item>My Item 1</md-menu-item>
        <md-menu-item>My Item 2</md-menu-item>
        <md-menu-item>My Item 3</md-menu-item>

        <md-menu-item>My Item 1</md-menu-item>
        <md-menu-item>My Item 2</md-menu-item>
        <md-menu-item>My Item 3</md-menu-item>
      </md-menu-content>
    </md-menu>
     
    </div>
     
  </b-col>
</template>
<script>
export default {
  name: "Categories",
  methods: {
  categoryClicked(item) {
      this.$emit('clicked-category', item)
    }
  }
  
};
</script>
<style scoped>
</style>