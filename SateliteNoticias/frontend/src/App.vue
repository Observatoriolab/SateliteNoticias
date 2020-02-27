<template>
  <div id="app">
    <div id="nav">
      <NavbarComponent />
      <router-view />
    </div>
  </div>
</template>

<script>
import NavbarComponent from "./components/NavBar.vue";
export default {
  name: "App",
  components: {
    NavbarComponent
  }
};
</script>
<style>
html,
body {
  height: 100%;
  font-family: "Playfair Display", serif;
}

.btn:focus {
  box-shadow: none !important;
}
</style>
