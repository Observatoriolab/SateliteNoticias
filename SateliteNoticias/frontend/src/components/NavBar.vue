<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{name: 'home'}" class="navbar-brand">Satelite de Noticias</router-link>

      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link :to="{name: 'home'}" class="btn btn-sm btn-success">Home</router-link>
          </li>
          <li class="nav-item mx-1">
            <router-link :to="{name: 'home'}" class="btn btn-sm btn-danger">Add Question</router-link>
          </li>
          <li class="nav-item">
            <a
              class="btn btn-sm btn-outline-secondary"
              href="/accounts/logout/"
              tabindex="-1"
              aria-disabled="true"
            >Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style >
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}

.navbar-brand:hover {
  color: red !important;
}
</style>