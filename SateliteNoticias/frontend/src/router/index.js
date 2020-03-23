import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import News from "../views/News.vue";
import NewsEditor from "../views/NewsEditor.vue";
import EditionEditor from "../views/EditionEditor.vue";
import NotFound from "../views/NotFound.vue";
import MainPage from "../mainComponents/MainPage.vue";
import fullNews from "../mainComponents/fullNews.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/news/:slug",
    name: "news",
    component: News,
    props: true
  },
  {
    path: "/ask",
    name: "news-editor",
    component: NewsEditor
  },
  {
    path: "/fullEdition",
    name: "news-fullEditor",
    component: fullNews
  },
  {
    path: "/edition/:id",
    name: "edition-editor",
    component: EditionEditor,
    props: true
  },
  {
    path: "*",
    name: "page-not-found",
    component: NotFound
  },
  {
    path: "/prueba",
    name: "MainPage",
    component: MainPage
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
