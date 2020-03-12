<template>
  <b-container fluid >
    <!-- BANNER COMPONENT -->
    <Banner></Banner>
    <!-- BANNER COMPONENT -->

    <b-row>
      <b-col md="12">
        <!-- WHOLE COMPONENT -->
        <b-row>
          <!-- CATEGORY COMPONENT -->
          <Categories></Categories>
          <!-- CATEGORY COMPONENT -->

          <b-col md="7">
            <!-- SEARCH BUTTONS COMPONENT -->
            <SearchButtons></SearchButtons>
            <!-- SEARCH BUTTONS COMPONENT -->

            <b-row>
              <News></News>
            </b-row>
          </b-col>

          <Edition></Edition>
        </b-row>
        <!-- WHOLE COMPONENT -->
      </b-col>
    </b-row>
  </b-container>
</template>>
<script>
import Banner from "@/miniComponents/main/Banner.vue";
import Categories from "@/miniComponents/main/Categories.vue";
import SearchButtons from "@/miniComponents/main/SearchButtons.vue";
import News from "./News.vue";
import Edition from "./Edition.vue";

export default {
  name: "MainPage",
  components: {
    Banner,
    Categories,
    SearchButtons,
    News,
    Edition
  }
};
</script>
<style scoped>

</style>>