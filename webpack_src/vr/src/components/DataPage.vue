<template>
	<div>
		<h1 class="text-center">Bevor es losgeht ...</h1>
		<br>
		<div class="alert alert-primary" role="alert">
			... brauchen wir ein paar Angaben zu Ihrer Person: <i>(* Pflichtfelder)</i>
		</div>

		<div class="form-row">
			<div class="form-group col-sm-4 col-md-2">
				<label for="inputGeburtsjahr">Geburtsjahr *</label>
				<input v-model="daten.geburtsjahr" type="number" min="1890" max="2020" :class="'form-control' + ((error.geburtsjahr.error) ? ' is-invalid' : ' is-valid')" id="inputGeburtsjahr" placeholder="Geburtsjahr">
				<div class="invalid-tooltip" v-if="error.geburtsjahr.changed">{{ error.geburtsjahr.msg }}</div>
			</div>
			<div class="form-group col-sm-8 col-md-4">
				<label>biologisches Geschlecht *</label>
				<div :class="'form-control' + ((error.bioGesch.error) ? ' is-invalid' : ' is-valid')" style="height: auto;">
					<div class="form-check form-check-inline" v-for="aCheck in [{val: 1, title: 'männlich', id: 'srman'}, {val: 2, title: 'weiblich', id: 'srwoman'}, {val: 3, title: 'andere', id: 'srsonst'}]">
						<input v-model="daten.bioGesch" class="form-check-input" type="radio" name="inputBioGesch" :id="aCheck.id" :value="aCheck.val">
						<label class="form-check-label" :for="aCheck.id">{{ aCheck.title }}</label>
					</div>
				</div>
			</div>
			<div class="form-group col-md-6">
				<label for="inputBeruf">Beruf *</label>
				<input v-model="daten.beruf" type="text" :class="'form-control' + ((error.beruf.error) ? ' is-invalid' : ' is-valid')" id="inputBeruf" placeholder="Beruf">
				<div class="invalid-tooltip" v-if="error.beruf.changed">{{ error.beruf.msg }}</div>
			</div>
		</div>
		<div class="form-row">
			<Wohnort v-model="daten.wohnort" class="col-md-6" :error="error.wohnort" :inputClass="((error.wohnort.error) ? ' is-invalid' : ' is-valid')" label="Aktueller Wohnort (inkl. Postleitzahl) *"/>
			<Wohnort v-model="daten.wohnortLeben" class="col-md-6" :error="error.wohnortLeben" :inputClass="((error.wohnortLeben.error) ? ' is-invalid' : ' is-valid')" label="Wo haben Sie den Großteil Ihres Lebens verbracht? (inkl. Postleitzahl) *"/>
		</div>
		<div class="form-group" style="position: relative;">
			<label for="inputSprachenDialekte">Mit welchen Sprachen / Dialekten sind Sie aufgewachsen? *</label>
			<input v-model="daten.sprachenDialekte" type="text" :class="'form-control' + ((error.sprachenDialekte.error) ? ' is-invalid' : ' is-valid')" id="inputSprachenDialekte" placeholder="Sprachen, Dialekte">
			<div class="invalid-tooltip" v-if="error.sprachenDialekte.changed">{{ error.sprachenDialekte.msg }}</div>
		</div>

		<div class="alert alert-success" role="alert">
			<h4 class="mb-3">Warum wollen wir das wissen?</h4>
			<p>Wir untersuchen, wie Menschen in Österreich Sprache verwenden, über Sprache denken und Sprache wahrnehmen. <b>Ihre Angaben helfen uns, Spracheinstellung in Österreich auszuwerten und besser zu verstehen.</b></p>
			<p class="mb-0"><b>Weitere Angaben zu Ihnen</b> helfen uns Ihren Beitrag besonders gut in das Gesamtbild einzuordnen.</p>
			<br>
			<button @click="weitereAngaben = true; checkErrors()" type="button" class="btn btn-lg btn-success w-100" v-if="!weitereAngaben">Weitere Angaben machen</button>
		</div>

		<div class="weitereangaben" v-if="weitereAngaben">
			<h4>Weitere Angaben: <button @click="weitereAngaben = false" type="button" class="btn btn-warning btn-sm float-right"><span class="d-none d-sm-block">Doch keine weiteren Angaben machen</span><span class="d-block d-sm-none">&times;</span></button></h4>
			<br>
			<p><b>Wo sind Ihre Eltern aufgewachsen?</b></p>
			<div class="form-row">
				<Wohnort v-model="daten.wohnortMutter" class="col-md-6" :error="error.wohnortMutter" :inputClass="((error.wohnortMutter.error) ? ' is-invalid' : ' is-valid')" label="Mutter (inkl. Postleitzahl) *"/>
				<Wohnort v-model="daten.wohnortVater" class="col-md-6" :error="error.wohnortVater" :inputClass="((error.wohnortVater.error) ? ' is-invalid' : ' is-valid')" label="Vater (inkl. Postleitzahl) *"/>
			</div>
			<RadioFromTo v-model="daten.sprachlichErzogenMutter" :error="error.sprachlichErzogenMutter" :inputClass="((error.sprachlichErzogenMutter.error) ? ' is-invalid' : ' is-valid')" label="Wie wurden Sie von Ihrem Mutter sprachlich erzogen? *" from="ausschließlich Dialekt" to="ausschließlich Hochdeutsch"/>
			<RadioFromTo v-model="daten.sprachlichErzogenVater" :error="error.sprachlichErzogenVater" :inputClass="((error.sprachlichErzogenVater.error) ? ' is-invalid' : ' is-valid')" label="Wie wurden Sie von Ihrem Vater sprachlich erzogen? *" from="ausschließlich Dialekt" to="ausschließlich Hochdeutsch"/>
			<div class="form-row">
				<div class="form-group col-md-4">
					<label>Beherrschen Sie selbst einen Dialekt? *</label>
					<div class="form-control">
						<div class="form-check form-check-inline" v-for="aCheck in [{val: 'Ja', title: 'Ja', id: 'inputDialektSelbstJa'}, {val: 'Nein', title: 'Nein', id: 'inputDialektSelbstNein'}]">
							<input v-model="daten.dialektSelbst" :class="'form-check-input' + ((error.dialektSelbst.error) ? ' is-invalid' : ' is-valid')" type="radio" name="inputDialektSelbst" :id="aCheck.id" :value="aCheck.val">
							<label class="form-check-label" :for="aCheck.id">{{ aCheck.title }}</label>
						</div>
					</div>
				</div>
				<div class="form-group col-md-8" v-if="daten.dialektSelbst === 'Ja'">
					<label for="inputDialektSelbstWelcher">Welchen Dialekt beherrschen Sie? *</label>
					<input v-model="daten.dialektSelbstWelcher" type="text" :class="'form-control' + ((error.dialektSelbstWelcher.error) ? ' is-invalid' : ' is-valid')" id="inputDialektSelbstWelcher" placeholder="Dialekt">
					<div class="invalid-tooltip" v-if="error.dialektSelbstWelcher.changed">{{ error.dialektSelbstWelcher.msg }}</div>
				</div>
			</div>
			<RadioFromTo v-model="daten.dialektSprechen" :error="error.dialektSprechen" :inputClass="((error.dialektSprechen.error) ? ' is-invalid' : ' is-valid')" label="Wie gut sprechen Sie diesen Dialekt? *" from="gar nicht" to="sehr gut" v-if="daten.dialektSelbst === 'Ja'"/>
			<RadioFromTo v-model="daten.dialektNutzen" :error="error.dialektNutzen" :inputClass="((error.dialektNutzen.error) ? ' is-invalid' : ' is-valid')" label="Wie häufig sprechen Sie Dialekt? *" from="nie" to="immer" v-if="daten.dialektSelbst === 'Ja'"/>
			<RadioFromTo v-model="daten.hochdeutschSprechen" :error="error.hochdeutschSprechen" :inputClass="((error.hochdeutschSprechen.error) ? ' is-invalid' : ' is-valid')" label="Wie gut sprechen Sie Hochdeutsch? *" from="gar nicht" to="sehr gut"/>
			<RadioFromTo v-model="daten.hochdeutschNutzen" :error="error.hochdeutschNutzen" :inputClass="((error.hochdeutschNutzen.error) ? ' is-invalid' : ' is-valid')" label="Wie häufig sprechen Sie Hochdeutsch? *" from="nie" to="immer"/>
			<RadioFromTo v-model="daten.alltagSprechen" :error="error.alltagSprechen" :inputClass="((error.alltagSprechen.error) ? ' is-invalid' : ' is-valid')" label="Wie sprechen Sie hauptsächlich in Ihrem Alltag? *" from="ausschließlich Dialekt" to="ausschließlich Hochdeutsch"/>
			<div class="form-group" v-if="daten.alltagSprechen > 1 && daten.alltagSprechen < 7">
				<label for="inputBezeichnungSprechweise">Wie bezeichnen Sie diese Sprechweise, die Sie hauptsächlich in Ihrem Alltag sprechen? *</label>
				<input v-model="daten.bezeichnungSprechweise" type="text" :class="'form-control' + ((error.bezeichnungSprechweise.error) ? ' is-invalid' : ' is-valid')" id="inputBezeichnungSprechweise" placeholder="">
				<div class="invalid-tooltip" v-if="error.bezeichnungSprechweise.changed">{{ error.bezeichnungSprechweise.msg }}</div>
			</div>
			<div :class="'form-group' + ((error.anmerkungen.empty) ? ' is-empty' : '')">
				<label for="inputAnmerkungen">Haben Sie noch Anmerkungen zu diesem Fragebogen?</label>
				<input v-model="daten.anmerkungen" type="text" class="form-control" id="inputAnmerkungen" placeholder="">
			</div>
		</div>

		<div class="alert alert-primary mt-3" role="alert">
			<h4 class="mb-3">Der SFB „Deutsch in Österreich“ behandelt Ihre Daten vertraulich und ausschließlich für wissenschaftliche Zwecke.</h4>
			<div class="form-group form-check bg-white p-3 px-5 mb-2 rounded">
				<input v-model="daten.dsgvo" type="checkbox" :class="'form-check-input' + ((error.dsgvo.error) ? ' is-invalid' : ' is-valid')" id="dsgvoCheck">
				<label class="form-check-label" for="dsgvoCheck">Ich erkläre mich damit einverstanden, dass meine personenbezogenen Daten - wie in der <a href="https://iam.dioe.at/datenschutz/" target="_blank">Datenschutzerklärung</a> beschrieben - vom SFB „Deutsch in Österreich: Variation – Kontakt – Perzeption“ wissenschaftlich ausgewertet werden und im Zuge dessen innerhalb des SFBs verwendet werden. Diese Einwilligung kann ich jederzeit widerrufen.</label>
				<div class="invalid-tooltip" v-if="error.dsgvo.changed">{{ error.dsgvo.msg }}</div>
			</div>
		</div>

		<div class="alert alert-danger mt-3" role="alert" v-if="errors > 0">
			<h5>Formular enthält Fehler:</h5>
			<ul class="mb-0">
				<li v-for="aError in error" v-if="aError.error">{{ aError.msg }}</li>
			</ul>
		</div>

		<button @click="nextStep()" type="button" class="btn btn-primary w-100" :disabled="errors > 0">Los geht’s</button>

		<div class="loading" v-if="saving">Speichere ...</div>

	</div>
</template>

<script>
import RadioFromTo from './formular/RadioFromTo'
import Wohnort from './formular/Wohnort'
import _ from 'lodash'

export default {
	name: 'DataPage',
	data () {
		return {
			weitereAngaben: false,
			saving: false,
			errors: 0,
			daten: {
				geburtsjahr: null,
				bioGesch: 0,
				beruf: '',
				wohnort: {
					ort: '',
					plz: ''
				},
				wohnortLeben: {
					ort: '',
					plz: ''
				},
				sprachenDialekte: '',
				// Weitere Angaben
				wohnortVater: {
					ort: '',
					plz: ''
				},
				wohnortMutter: {
					ort: '',
					plz: ''
				},
				sprachlichErzogenVater: 0,
				sprachlichErzogenMutter: 0,
				dialektSelbst: '',
				dialektSelbstWelcher: '',
				dialektSprechen: 0,
				dialektNutzen: 0,
				hochdeutschSprechen: 0,
				hochdeutschNutzen: 0,
				alltagSprechen: 0,
				bezeichnungSprechweise: '',
				anmerkungen: '',
				dsgvo: false
			},
			error: {
				geburtsjahr: {
					check: function (val) { return (val >= 1890 && val <= 2020) },
					msg: 'Geburtsjahr muss nach 1890 liegen und vierstellig angegeben werden!'
				},
				bioGesch: {
					check: function (val) { return (val > 0 && val < 4) },
					msg: 'Bitte geben Sie Ihr Geschlecht an!'
				},
				beruf: {
					check: function (val) { return val },
					msg: 'Bitte geben Sie Ihren Beruf an!'
				},
				wohnort: {
					check: function (val) { return val.ort && val.plz },
					msg: 'Bitte geben Sie Ihren Wohnort mit gültiger Postleitzahl an!'
				},
				wohnortLeben: {
					check: function (val) { return val.ort && val.plz },
					msg: 'Bitte geben Sie den Wohnort, an dem Sie den Großteil Ihres Lebens verbracht haben, mit gültiger Postleitzahl an!'
				},
				sprachenDialekte: {
					check: function (val) { return val },
					msg: 'Bitte geben Sie an mit welchen Sprachen / Dialekten Sie aufgewachsen sind!'
				},
				// Weitere Angaben
				wohnortVater: {
					check: function (val, weitere) { return (val.ort && val.plz) || !weitere },
					msg: 'Bitte geben Sie den Wohnort Ihres Vaters mit gültiger Postleitzahl an!'
				},
				wohnortMutter: {
					check: function (val, weitere) { return (val.ort && val.plz) || !weitere },
					msg: 'Bitte geben Sie den Wohnort Ihrer Mutter mit gültiger Postleitzahl an!'
				},
				sprachlichErzogenVater: {
					check: function (val, weitere) { return val || !weitere },
					msg: 'Bitte geben Sie an wie Sie von Ihrem Vater sprachlich erzogen wurden!'
				},
				sprachlichErzogenMutter: {
					check: function (val, weitere) { return val || !weitere },
					msg: 'Bitte geben Sie an wie Sie von Ihrer Mutter sprachlich erzogen wurden!'
				},
				dialektSelbst: {
					check: function (val, weitere) { return val || !weitere },
					msg: 'Bitte geben Sie an ob Sie selbst einen Dialekt beherrschen!'
				},
				dialektSelbstWelcher: {
					check: function (val, weitere, daten) { return val || !weitere || daten.dialektSelbst !== 'Ja' },
					msg: 'Bitte geben Sie an welchen Dialekt Sie beherrschen!'
				},
				dialektSprechen: {
					check: function (val, weitere, daten) { return val || !weitere || daten.dialektSelbst !== 'Ja' },
					msg: 'Bitte geben Sie an wie gut Sie diesen Diallekt sprechen!'
				},
				dialektNutzen: {
					check: function (val, weitere, daten) { return val || !weitere || daten.dialektSelbst !== 'Ja' },
					msg: 'Bitte geben Sie an wie häufig Sie diesen Diallekt sprechen!'
				},
				hochdeutschSprechen: {
					check: function (val, weitere) { return val || !weitere },
					msg: 'Bitte geben Sie an wie gut Sie Hochdeutsch sprechen!'
				},
				hochdeutschNutzen: {
					check: function (val, weitere) { return val || !weitere },
					msg: 'Bitte geben Sie an wie häufig Sie Hochdeutsch sprechen!'
				},
				alltagSprechen: {
					check: function (val, weitere) { return val || !weitere },
					msg: 'Bitte geben Sie an wie Sie hauptsächlich in Ihrem Alltag sprechen!'
				},
				bezeichnungSprechweise: {
					check: function (val, weitere, daten) { return val || !weitere || (daten.alltagSprechen < 2 || daten.alltagSprechen > 6) },
					msg: 'Bitte geben Sie an wie Sie Ihre Sprechweise bezeichnen!'
				},
				dsgvo: {
					check: function (val, weitere) { return val },
					msg: 'Bitte stimmen Sie der Verarbeitung Ihrer personenbezogenen Daten zu!'
				},
			}
		}
	},
	watch: {
		'weitereAngaben' (nVal) {
			this.debouncedCheckErrors()
		},
	},
	methods: {
		checkErrors () {
			this.errors = 0
			Object.keys(this.daten).forEach(function (aKey) {
				this.checkError(aKey)
				if (this.error[aKey].error) {
					this.errors += 1
				}
			}, this)
		},
		checkError (aKey, uVal = undefined) {
			let cVal = uVal
			if (cVal === undefined) {
				cVal = this.daten[aKey]
			}
			if (!this.error[aKey]) {
				this.error[aKey] = {}
			}
			this.$set(this.error[aKey], 'error', false)
			if (this.error[aKey].check) {
				if (!this.error[aKey].check(cVal, this.weitereAngaben, this.daten)) {
					this.$set(this.error[aKey], 'error', true)
				}
			}
			this.$set(this.error[aKey], 'empty', true)
			if (cVal) {
				if (typeof cVal === 'object') {
					Object.keys(cVal).some(function (aProp) {
						if (cVal[aProp]) {
							this.$set(this.error[aKey], 'empty', false)
							return true
						}
					}, this)
				} else {
					this.$set(this.error[aKey], 'empty', false)
				}
			}
		},
		debouncedCheckErrors: _.debounce(function () {
			this.checkErrors()
		}, 250),
		initCheckErrors () {
			this.checkErrors()
			Object.keys(this.error).forEach(function (aKey) {
				if (this.daten[aKey] && typeof this.daten[aKey] === 'object') {
					Object.keys(this.daten[aKey]).forEach(function (aProp) {
						if (this.daten[aKey][aProp] || this.daten[aKey][aProp] === 0 || this.daten[aKey][aProp] === '') {
							this.$watch('daten.' + aKey + '.' + aProp, function (nVal) { this.$nextTick(() => { this.$set(this.error[aKey], 'changed', true); this.debouncedCheckErrors() }) })
						}
					}, this)
				} else {
					this.$watch('daten.' + aKey, function (nVal) { this.$nextTick(() => { this.$set(this.error[aKey], 'changed', true); this.debouncedCheckErrors() }) })
				}
			}, this)
		},
		nextStep () {
			if (this.errors === 0) {
				this.$emit('savedata', JSON.parse(JSON.stringify(this.daten)), this.weitereAngaben)
				this.saving = true
			} else {
				alert('Das Formular enthält noch Fehler!')
			}
		},
	},
	mounted () {
		this.initCheckErrors()
	},
	components: {
		RadioFromTo,
		Wohnort,
	},
}
</script>

<style scoped>
	.weitereangaben {
		position: relative;
		margin-top: 30px;
		margin-bottom: 30px;
		padding-top: 15px;
		padding-bottom: 1px;
	}
	.weitereangaben:before, .weitereangaben:after {
		content: "";
		position: absolute;
		background: #d4edda;
		left: -15px;
		top: 0px;
		bottom: 0px;
		width: 3px;
	}
	.weitereangaben:after {
		left: inherit;
		right: -15px;
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
