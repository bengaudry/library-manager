<script setup>
  import { ref } from 'vue'

  const form = ref({
    username: '',
    email: '',
    password: ''
  })

  const message = ref('')

  const handleRegister = async () => {
    try {
      const response = await fetch('http://localhost:5000/backend/app/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form.value)
      })

      const result = await response.json()
      message.value = result.message

      if (response.ok) {
        form.value = { username: '', email: '', password: '' }
      }
    } catch (error) {
      message.value = "Erreur de connexion au serveur"
    }
  }
</script>

<template>
    <div class="register-container">
      <h1>Inscription</h1>

      <router-link to="/">Retour</router-link>

      <form @submit.prevent="handleRegister">
        <input v-model="form.username" type="text" placeholder="Nom d'utilisateur" required />
        <input v-model="form.email" type="email" placeholder="Email" required />
        <input v-model="form.password" type="password" placeholder="Mot de passe" required />
        <button type="submit">S'inscrire</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>


</template>

<style scoped>
    input {
        display: block;
        width: 90%;
        padding: 10px;
        margin-bottom: 15px;
    }

    button {
        background-color: green;
        color: white;
        width: 10%;
        height: 25px;
        border: 0px;
    }
</style>