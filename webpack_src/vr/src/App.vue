<template>
	<div id="app">
		<div class="content">
			<StartPage @start="start()" v-if="site === 0"/>
			<DataPage v-if="site === 1"/>
		</div>
	</div>
</template>

<script>
	/* global csrf */
	import StartPage from './components/StartPage'
	import DataPage from './components/DataPage'

	export default {
		name: 'App',
		http: {
			root: '/data',
			headers: {
				'X-CSRFToken': csrf
			},
			emulateJSON: true
		},
		data () {
			return {
				site: 0,
				playerId: 0,
			}
		},
		mounted () {
		},
		methods: {
			start () {		// Wenn noch keine playerId dann zum Fragebogen für Sozialdaten, sonst weiter zum Spiel ...
				this.site = ((this.playerId === 0) ? 1 : 2)
			},
		},
		components: {
			StartPage,
			DataPage,
		},
	}
</script>

<style>
</style>
