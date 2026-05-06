import { createRouter, createWebHistory } from "vue-router";
import BookListView from "../views/BookListView.vue";

const routes = [
    {
        path: "/",
        name: "books",
        component: BookListView,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
