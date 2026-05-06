<template>
    <div class="book-page">
        <h1>
            Livres disponibles
        </h1>

        <div v-if="loading">
            Chargement...
        </div>

        <div v-else class="book-list">
            <div v-for="book in books" :key="book.id" class="book-card">
                <h3>
                    {{ book.title }}
                </h3>
                <p>
                    Auteur : {{ book.author }}
                </p>
                <p>
                    Emplacement : {{ book.location }}
                </p>
                <p>
                    Exemplaires : {{ book.copies }}
                </p>

                <p v-if="book.copies > 0 && !book.reserved">
                    Disponible
                </p>

                <p v-if="book.copies === 0 && !book.reserved">
                    Indisponible
                </p>

                <p v-if="book.reserved">
                    Réservé
                </p>

                <button v-if="book.copies > 0 && !book.reserved" @click="reserveBook(book.id)">
                    Réserver
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "BookListView",
        data() {
            return {
                books: [],
                loading: true,
            };
        },
        async mounted() {
            await this.fetchBooks();
        },
        methods: {
            async fetchBooks() {
                try {
                    const res = await fetch("http://localhost:5000/books");
                    this.books = await res.json();
                } catch (e) {
                    console.error("Erreur API:", e);
                } finally {
                    this.loading = false;
                }
            },

            async reserveBook(bookId) {
                try {
                    const res = await fetch(`http://localhost:5000/reserve/${bookId}`, {
                        method: "POST",
                    });

                    const updatedBook = await res.json();

                    this.books = this.books.map(b =>
                        b.id === updatedBook.id
                            ? { ...updatedBook, reserved: true }
                            : b
                    );

                } catch (e) {
                    console.error("Erreur réservation:", e);
                }
            }
        },
    };
</script>

<style scoped>
    .book-list {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
        gap: 12px;
    }

    .book-card {
        border: 1px solid #ddd;
        padding: 12px;
        border-radius: 8px;
    }
</style>
