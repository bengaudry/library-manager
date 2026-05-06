import {createRouter, createMemoryHistory} from "vue-router";

const routes = [
    { path: "/", component: () => import("../views/Accueil.vue") },
    { path: "/gestionnaire/reservations", component: () => import("../views/gestionnaire/Reservations.vue") },
    { path: "/ouvrages", component: () => import("../views/Ouvrages.vue") },
    { path: "/lecteur/reservations", component: () => import("../views/lecteur/Reservations.vue") },
]

export const router = createRouter({
    history: createMemoryHistory(),
    routes
})
