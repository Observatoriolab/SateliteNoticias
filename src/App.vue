<template>
  <div id="app" class="stop-scrolling">
    <div id="nav">
      <!-- <NavbarComponent /> -->
      <router-view />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "App",
  components: {
  },

  methods: {
    //En ves de usar .then, dejarlo asincrono
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      //Lo deje en el local storage del browser para ser usado y corroborar que es el usuario
      window.localStorage.setItem("username", requestUser);
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
.stop-scrolling {
  height: 100%;
  overflow: hidden;
}
</style>
