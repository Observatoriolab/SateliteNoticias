<template>
  <b-navbar toggleable="lg" type="dark" variant="info">

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav  style="position:relative, align-items:center">
           <h3 style="float:right">Satelite de Noticias</h3> 

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>{{requestUser}}</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="/accounts/logout/">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<script>
export default {
  name: "Banner",
   data() {
    return {    
      requestUser: null
    };
  },

  created(){
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    
  }
};
</script>
<style lang="stylus"></style>
