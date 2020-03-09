<template>
  <div id="app">
    <div id="nav">
      <NavbarComponent />
      <router-view />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import NavbarComponent from "@/components/NavBar.vue";
export default {
  name: "App",
  components: {
    NavbarComponent
  },

  methods: {
    //En ves de usar .then, dejarlo asincrono
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      //Lo deje en el local storage del browser para ser usado y corroborar que es el usuario
      window.localStorage.setItem("username", requestUser);
      //console.log(data)
      //console.log(requestUser)
    }
  },
  created() {
    this.setUserInfo();
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
