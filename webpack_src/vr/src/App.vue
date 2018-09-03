<template>
	<div id="app">
		<StartPage/>
	</div>
</template>

<script>
	/* global csrf */
	import StartPage from './components/StartPage'

	export default {
		name: 'App',
		mounted () {
			console.log(csrf)
		},
		components: {
			StartPage
		}
	}
</script>

<style>
</style>
