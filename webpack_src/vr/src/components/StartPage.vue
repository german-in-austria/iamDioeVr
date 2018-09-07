<template>
	<div class="text-center">
		<h1>I am DiÖ - Varietäten raten</h1>
		<br>
		<button @click="$emit('start')" type="button" class="btn btn-primary">Starten ...</button>
	</div>
</template>

<script>
	export default {
		name: 'StartPage',
		data () {
			return {
			}
		},
	}
</script>

<style scoped>
</style>
