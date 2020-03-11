import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import News from "../views/News.vue";
import NewsEditor from "../views/NewsEditor.vue";
import EditionEditor from "../views/EditionEditor.vue";
import NotFound from "../views/NotFound.vue";
import Tryout from "../tryouts/vistaPrincipal.vue";

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
    name: "vistaPrincipal",
    component: Tryout
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
