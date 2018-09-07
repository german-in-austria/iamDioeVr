<template>
	<div id="app">
		<div class="content">
			<StartPage @start="start()" v-if="site === 0"/>
			<DataPage @savedata="saveData" v-if="site === 1"/>
			<GamePage @getGameData="getGameData" @saveGameRound="saveGameRound" @savedataSe="savedataSe" @getAuswertungsData="getAuswertungsData" v-if="site === 2"/>
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
				playerUuId: null,
			}
		},
		mounted () {
			if (this.devMode) {
				console.log(mediaUrl, gData)
				this.playerUuId = '2c8dd99b-3b42-48a7-9cd6-df63f5b2122f'
			}
		},
		methods: {
			start () {		// Wenn noch keine playerUuId dann zum Fragebogen für Sozialdaten, sonst weiter zum Spiel ...
				this.site = ((this.playerUuId) ? 2 : 1)
			},
			saveData (data, weitere) {
				this.$http.post('', {
					set: 'playerData',
					data: JSON.stringify({'data': data, 'weitere': weitere})
				})
				.then((response) => {
					if (response.data.playerUuId) {
						this.playerUuId = response.data.playerUuId
						this.site = 2
					} else {
						console.log(response.data)
						alert('Fehler! Keine "uuId" erhalten!')
					}
				})
				.catch((err) => {
					console.log(err)
					alert('Fehler!')
				})
			},
			savedataSe (data) {
				this.$http.post('', {
					set: 'playerDataSe',
					playerUuId: this.playerUuId,
					data: JSON.stringify({'data': data})
				})
				.then((response) => {
					console.log(response.data)
				})
				.catch((err) => {
					console.log(err)
					alert('Fehler!')
				})
			},
			saveGameRound (data) {
				this.$set(data, 'saving', true)
				this.$http.post('', {
					set: 'gameRound',
					playerUuId: this.playerUuId,
					data: JSON.stringify(data.data)
				})
				.then((response) => {
					if (this.playerUuId === response.data.playerUuId) {
						this.$set(data, 'saving', false)
					} else {
						console.log(response.data)
						alert('Fehler! "uuId" stimmt nicht überein!')
					}
				})
				.catch((err) => {
					console.log(err)
					alert('Fehler!')
				})
			},
			getAuswertungsData (target) {
				this.$set(target, 'auswertung', {})
				this.$set(target.auswertung, 'ready', false)
				this.$set(target.auswertung, 'loading', true)
				this.$http.post('', {
					get: 'auswertungsData',
					playerUuId: this.playerUuId,
				})
				.then((response) => {
					this.$set(target.auswertung, 'loading', false)
					if (this.playerUuId === response.data.playerUuId) {
						this.$set(target.auswertung, 'ready', true)
						if (this.devMode) {
							console.log(JSON.parse(JSON.stringify(response.data)))
						}
						this.$set(target.auswertung, 'data', response.data)
					} else {
						console.log(response.data)
						alert('Fehler! "uuId" stimmt nicht überein!')
					}
				})
				.catch((err) => {
					console.log(err)
					this.$set(target.auswertung, 'loading', false)
					alert('Fehler!')
				})
			},
			getGameData (target) {
				this.$set(target, 'game', {})
				this.$set(target.game, 'ready', false)
				this.$set(target.game, 'loading', true)
				this.$http.post('', {
					get: 'gameData',
					playerUuId: this.playerUuId,
				})
				.then((response) => {
					this.$set(target.game, 'loading', false)
					if (this.playerUuId === response.data.playerUuId) {
						this.$set(target.game, 'ready', true)
						if (this.devMode) {
							console.log(JSON.parse(JSON.stringify(response.data)))
						}
						this.$set(target.game, 'data', response.data)
					} else {
						console.log(response.data)
						alert('Fehler! "uuId" stimmt nicht überein!')
					}
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
	html {
		font-size: 1.1rem;
	}
	.content {
		padding-top: 20px;
		padding-bottom: 30px;
	}
	.is-empty .form-control {
		border-color: #5aaaff;
	}
</style>
