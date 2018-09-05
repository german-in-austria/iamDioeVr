<template>
	<div id="app">
		<div class="content">
			<StartPage @start="start()" v-if="site === 0"/>
			<DataPage @savedata="saveData" v-if="site === 1"/>
			<GamePage @getGameData="getGameData" v-if="site === 2"/>
		</div>
	</div>
</template>

<script>
	/* global csrf mediaUrl gData */
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
			if (this.devMode) {
				console.log(mediaUrl, gData)
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
			},
			getGameData (target) {
				this.$set(target, 'game', {})
				this.$set(target.game, 'ready', false)
				this.$set(target.game, 'loading', true)
				this.$http.post('', {
					get: 'gameData',
					playerId: this.playerId,
				})
				.then((response) => {
					this.$set(target.game, 'loading', false)
					this.$set(target.game, 'ready', true)
					this.$set(target.game, 'data', response.data)
				})
				.catch((err) => {
					console.log(err)
					this.$set(target.game, 'loading', false)
					alert('Fehler!')
				})
			},
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
