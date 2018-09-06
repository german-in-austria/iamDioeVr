<template>
	<div>
		<div class="card" v-if="gameData.game && !gameData.game.loading && gameData.game.ready && gameData.game.data">
			<div class="card-header text-white bg-primary text-center">
				<div class="d-flex mb-2">
					<div>Runde {{ rundeNr + 1 }}</div>
					<div class="mx-auto">Sprachbeispiel {{ beispielNr + 1 }}</div>
					<div class="hidden">Runde {{ rundeNr + 1 }}</div>
				</div>
				<button  type="button" class="btn btn-sm btn-light" disabled v-if="!loaded">Lade Audio ...</button>
				<button @click="abspielen()" type="button" class="btn btn-sm btn-light" :disabled="playing" v-else-if="played < 2">{{ ((playing) ? 'Wiedergabe ...' : ((played === 0) ? 'Abspielen' : 'Noch einmal hören?')) }}</button>
				<button @click="" type="button" class="btn btn-sm btn-light" disabled v-else>Kann nur zwei mal angehört werden</button>
			</div>
			<div class="card-body" style="background: #eee;">
				<div @click="selectOrt(aOrt.s)" :class="'ort-btn' + ((selOrt === aOrt.s) ? ' selected' : '')" v-for="aOrt in gData.orte">{{ aOrt.s }} - {{ aOrt.t }}</div>
			</div>
			<div class="card-body">
				<RadioFromTo v-model="sympathie" label="Das Gehörte wirkt auf mich:" from="sympathisch" to="unsympathisch" :disabled="played === 0"/>
			</div>
			<div class="card-footer text-white bg-primary text-right">
				<button @click="weiter()" type="button" class="btn btn-sm btn-light" :disabled="played === 0 || sympathie === 0 || !selOrt">Weiter</button>
			</div>
		</div>
		<div class="loading" v-if="loading">Lade ...</div>
		<div class="loading" v-if="saveData.saving">Speichere ...</div>
		<audio ref="audioplayer"><source :src="mediaUrl + gameData.game.data[['S', 'D'][rundeNr]][beispielNr].file" type="audio/ogg" v-if="gameData.game && !gameData.game.loading && gameData.game.ready && gameData.game.data"></audio>
	</div>
</template>

<script>
	/* global alert gData mediaUrl */
	import RadioFromTo from '../formular/RadioFromTo'

	export default {
		name: 'Game',
		data () {
			return {
				beispielNr: 0,
				rundeNr: 0,
				played: 0,
				sympathie: 0,
				selOrt: null,
				gData: gData,
				gameData: {},
				mediaUrl: mediaUrl,
				loading: false,
				audio: undefined,
				playing: false,
				loaded: false,
				audioReload: false,
				saveData: {'saving': false, 'data': {}},
			}
		},
		watch: {
			'audioReload' (nVal) {
				if (nVal) {
					this.$nextTick(function () {
						this.audioReload = false
						this.audio.load()
					})
				}
			},
			'saveData.saving' (nVal) {
				if (!nVal) {
					this.$set(this.saveData, 'data', {})
					this.beispielNr += 1
					if (this.beispielNr > 2) {
						this.beispielNr = 0
						this.rundeNr += 1
						if (this.rundeNr > 1) {
							this.rundeNr = 0
							this.$emit('gameEnd')
						}
					}
					this.played = 0
					this.sympathie = 0
					this.selOrt = null
					this.playing = false
					this.audioReload = true
				}
			},
		},
		methods: {
			weiter () {
				let sData = {
					'beispielNr': this.beispielNr,
					'rundeNr': this.rundeNr,
					'selOrt': this.selOrt,
					'sympathie': this.sympathie,
					'played': this.played,
					'gId': this.gameData.game.data.gId,
					'aId': this.gameData.game.data[['S', 'D'][this.rundeNr]][this.beispielNr].pk,
				}
				this.$set(this.saveData, 'data', sData)
				this.$emit('saveGameRound', this.saveData)
			},
			selectOrt (sOrt) {
				if (this.played > 0) {
					this.selOrt = sOrt
				}
			},
			audioLoaded () {
				if (this.audio.readyState >= 2) {
					this.loaded = true
				} else {
					this.playing = false
					this.loaded = false
					alert('Audiodatei konnte nicht geladen werden!')
					throw new Error('Audiodatei konnte nicht geladen werden!')
				}
			},
			abspielen () {
				this.played += 1
				this.audio.play()
			},
			audioPlayPause: function (e) {
				this.playing = (e.type === 'play')
			},
		},
		mounted () {
			this.$emit('getGameData', this.gameData)
			this.audio = this.$refs.audioplayer
			this.audio.addEventListener('loadeddata', this.audioLoaded)
			this.audio.addEventListener('pause', this.audioPlayPause)
			this.audio.addEventListener('play', this.audioPlayPause)
		},
		beforeDestroy () {
			// clearInterval(this.audioInterval);
			this.audio.removeEventListener('loadeddata', this.audioLoaded)
			this.audio.removeEventListener('pause', this.audioPlayPause)
			this.audio.removeEventListener('play', this.audioPlayPause)
		},
		components: {
			RadioFromTo,
		},
	}
</script>

<style scoped>
	.ort-btn {
		background: #ddd;
		margin: 5px;
		padding: 0px 5px;
		cursor: pointer;
	}
	.ort-btn.selected {
		background: #ccf;
	}
	.ort-btn:hover {
		background: #dde;
	}
	.hidden {
		visibility: hidden;
	}
	.loading {
		position: fixed;
		left: 0;
		top: 0;
		right: 0;
		bottom: 0;
		padding-top: 40vh;
		text-align: center;
		color: #fff;
		background: #000;
		background: rgba(0,0,0,0.5);
		font-size: 60px;
	}
</style>
