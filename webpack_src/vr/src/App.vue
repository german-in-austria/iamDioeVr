<template>
	<div id="app">
		<div class="content">
			<StartPage @start="start()" v-if="site === 0"/>
			<DataPage @savedata="saveData" v-if="site === 1"/>
			<GamePage v-if="site === 2"/>
		</div>
	</div>
</template>

<script>
	/* global csrf gData */
	import StartPage from './components/StartPage'
	import DataPage from './components/DataPage'
	import GamePage from './components/GamePage'

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
				devMode: (process.env.NODE_ENV === 'development'),
				site: 0,
				playerId: null,
			}
		},
		mounted () {
			console.log(gData)
			if (this.devMode) {
				this.playerId = -1
			}
		},
		methods: {
			start () {		// Wenn noch keine playerId dann zum Fragebogen für Sozialdaten, sonst weiter zum Spiel ...
				this.site = ((this.playerId) ? 2 : 1)
			},
			saveData (data, weitere) {
				// ToDo: Speichervorgang und playerId vergeben
				console.log(JSON.stringify(data))
				console.log(data, weitere)
			}
		},
		components: {
			StartPage,
			DataPage,
			GamePage,
		},
	}
</script>

<style>
	.content {
		padding-bottom: 50px;
		padding-top: 20px;
	}
	.is-empty .form-control {
		border-color: #5aaaff;
	}
</style>
