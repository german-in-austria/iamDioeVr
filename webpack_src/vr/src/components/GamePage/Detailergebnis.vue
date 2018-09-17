<template>
	<div class="text-center">
		<h1>Detailergebnis</h1>
		<br>
		<div v-if="auswertungsData.auswertung && auswertungsData.auswertung.ready && auswertungsData.auswertung.data">
			<p>Sie haben <b>{{ auswertungsData.auswertung.data.antwortenRichtigDr }}</b> von <b>{{ auswertungsData.auswertung.data.antworten }}</b> Sprecherinnen und Sprechern richtig ihren <b>Dialektregionen</b> zugeordnet.<br>
			Sie haben <b>{{ auswertungsData.auswertung.data.antwortenRichtigBl }}</b> von <b>{{ auswertungsData.auswertung.data.antworten }}</b> Sprecherinnen und Sprechern richtig ihren <b>Bundesländern</b> zugeordnet.<br>
			Sie haben <b>{{ auswertungsData.auswertung.data.antwortenRichtig }}</b> von <b>{{ auswertungsData.auswertung.data.antworten }}</b> Sprecherinnen und Sprechern richtig ihren <b>Heimatorten</b> zugeordnet.</p>
			<p>Im Vergleich mit anderen Spielenden liegen sie damit hier:</p>
			<div>
				<svg viewBox="-5 -5 410 210" class="border">
					<line x1="0" x2="400" :y1="(y - 1) * 18 + 0.5" :y2="(y - 1) * 18 + 0.5" style="stroke: #eee; stroke-width: 0.5;" v-for="y in 11"/>
					<g :transform="'translate(' + (40 + x * 80) + ' 180)'" v-for="(y, x) in auswertungsData.auswertung.data.statistik">
						<rect x="-20" width="10" :y="0.5 + -180 / statistikMax.Dr * y.Dr" :height="180 / statistikMax.Dr * y.Dr" :class="'chart chartdr' + ((auswertungsData.auswertung.data.richtigeKlasseDr === x + 1) ? ' active' : '')"/>
						<rect x="-5" width="10" :y="0.5 + -180 / statistikMax.Bl * y.Bl" :height="180 / statistikMax.Bl * y.Bl" :class="'chart chartbl' + ((auswertungsData.auswertung.data.richtigeKlasseBl === x + 1) ? ' active' : '')"/>
						<rect x="10" width="10" :y="0.5 + -180 / statistikMax.Ho * y.Ho" :height="180 / statistikMax.Ho * y.Ho" :class="'chart chartho' + ((auswertungsData.auswertung.data.richtigeKlasse === x + 1) ? ' active' : '')"/>
						<text x="0" y="15" text-anchor="middle" style="font-size: 8px">{{ ['0%-20% richtig', '20%-40% richtig', '40%-60% richtig', '60%-80% richtig', '80%-100% richtig'][x] }}</text>
					</g>
				</svg>
			</div>
			<br>
			<p><span class="colbox colboxdr">&nbsp;</span> = Dialektregion, <span class="colbox colboxbl">&nbsp;</span> = Bundesland, <span class="colbox colboxho">&nbsp;</span> = Heimatort<br></p>
			<br>
			<p><b>"Hochdeutsch" vs Dialekt</b></p>
			<p v-if="auswertungsData.auswertung.data.antwortenDialektRichtig === auswertungsData.auswertung.data.antwortenStandardRichtig">Egal ob "Hochdeutsch" oder Dialekt, Sie erkennen die Sprecherinnen und Sprecher gleich gut.</p>
			<p v-else>Ihnen fällt es leichter die Sprecherinnen und Sprecher richtig zu zuordnen,<br>
				wenn diese <b>{{ ((auswertungsData.auswertung.data.antwortenDialektRichtig > auswertungsData.auswertung.data.antwortenStandardRichtig) ? 'Dialekt' : '"Hochdeutsch"') }}</b> sprechen.</p>
			<p>(<b>Dialektregion: </b><b>{{ auswertungsData.auswertung.data.antwortenStandardRichtigDr }}</b> "Hochdeutsch" richtig zugeordnet | <b>{{ auswertungsData.auswertung.data.antwortenDialektRichtigDr }}</b> Dialekt richtig zugeornet)<br>
				(<b>Bundesland: </b><b>{{ auswertungsData.auswertung.data.antwortenStandardRichtigBl }}</b> "Hochdeutsch" richtig zugeordnet | <b>{{ auswertungsData.auswertung.data.antwortenDialektRichtigBl }}</b> Dialekt richtig zugeornet)<br>
				(<b>Heimatort: </b><b>{{ auswertungsData.auswertung.data.antwortenStandardRichtig }}</b> "Hochdeutsch" richtig zugeordnet | <b>{{ auswertungsData.auswertung.data.antwortenDialektRichtig }}</b> Dialekt richtig zugeornet)</p>
			<p><b>Jung vs Alt</b></p>
			<p v-if="auswertungsData.auswertung.data.antwortenJungRichtig === auswertungsData.auswertung.data.antwortenAltRichtig">Egal ob jung oder alt, Sie erkennen die Sprecherinnen und Sprecher gleich gut.</p>
			<p v-else>Es fällt Ihnen leichter <b>{{ ((auswertungsData.auswertung.data.antwortenJungRichtig > auswertungsData.auswertung.data.antwortenAltRichtig) ? 'junge' : 'alte') }}</b> Sprecherinnen und Sprecher richtig zu zuordnen.</p>
			<p>(<b>Dialektregion: </b><b>{{ auswertungsData.auswertung.data.antwortenJungRichtigDr }}</b> junge Menschen richtig zugeordnet | <b>{{ auswertungsData.auswertung.data.antwortenAltRichtigDr }}</b> alte Menschen richtig zugeordnet)<br>
			(<b>Bundesland: </b><b>{{ auswertungsData.auswertung.data.antwortenJungRichtigBl }}</b> junge Menschen richtig zugeordnet | <b>{{ auswertungsData.auswertung.data.antwortenAltRichtigBl }}</b> alte Menschen richtig zugeordnet)<br>
			(<b>Heimatort: </b><b>{{ auswertungsData.auswertung.data.antwortenJungRichtig }}</b> junge Menschen richtig zugeordnet | <b>{{ auswertungsData.auswertung.data.antwortenAltRichtig }}</b> alte Menschen richtig zugeordnet)</p>
			<p><b>Danke, dass Sie mitgespielt haben!</b></p>
		</div>
		<br>
		<button @click="$emit('next')" type="button" class="btn btn-primary">Ende</button><br><br>
		<div class="loading" v-if="!(auswertungsData.auswertung && auswertungsData.auswertung.ready)">Lade ... <button @click="reload()" v-if="devMode" style="font-size:20px;">Reload</button></div>
		<button @click="reload()" v-if="devMode">Reload</button>
	</div>
</template>

<script>
	export default {
		name: 'Detailergebnis',
		data () {
			return {
				devMode: (process.env.NODE_ENV === 'development'),
				auswertungsData: {},
			}
		},
		computed: {
			statistikMax () {
				let aMax = 0
				let aMaxBl = 0
				let aMaxDr = 0
				this.auswertungsData.auswertung.data.statistik.forEach(function (x) {
					if (x['Ho'] > aMax) {
						aMax = x['Ho']
					}
					if (x['Bl'] > aMaxBl) {
						aMaxBl = x['Bl']
					}
					if (x['Dr'] > aMaxDr) {
						aMaxDr = x['Dr']
					}
				}, this)
				return {'Ho': aMax, 'Bl': aMaxBl, 'Dr': aMaxDr}
			},
		},
		watch: {
			'auswertungsData' (nVal) {
				if (nVal) {
					if (this.devMode) {
						console.log(this.auswertungsData)
					}
				}
			},
		},
		methods: {
			reload () {
				this.loading = true
				this.auswertungsData = {}
				this.$emit('getAuswertungsData', this.auswertungsData)
			},
		},
		mounted () {
			this.reload()
		},
	}
</script>

<style scoped>
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
	rect.chartdr {
		fill: #ffc107;
	}
	rect.chartbl {
		fill: #007bff;
	}
	rect.chartho {
		fill: #28a745;
	}
	rect.chart.active {
		stroke-width: 1;
		stroke: #dc3545;
	}
	.colbox {
		display: inline-block;
		width: 26px;
	}
	.colboxdr {
		background: #ffc107;
	}
	.colboxbl {
		background: #007bff;
	}
	.colboxho {
		background: #28a745;
	}
</style>
