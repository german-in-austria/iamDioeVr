<template>
	<div>
		<h1>Sozialdaten</h1>
		<br>
		<div class="alert alert-primary" role="alert">
			Bevor es losgeht, brauchen wir ein paar Angaben zu Ihrer Person:
		</div>

		<div class="form-row">
			<div class="form-group col-sm-4 col-md-2">
				<label for="inputGeburtsjahr">Geburtsjahr</label>
				<input v-model="daten.geburtsjahr" type="number" class="form-control" id="inputGeburtsjahr" placeholder="Geburtsjahr">
			</div>
			<div class="form-group col-sm-8 col-md-4">
				<label>biologisches Geschlecht</label>
				<div class="form-control">
					<div class="form-check form-check-inline" v-for="aCheck in [{val: 1, title: 'männlich', id: 'srman'}, {val: 2, title: 'weiblich', id: 'srwoman'}, {val: 3, title: 'sonstiges', id: 'srsonst'}]">
						<input v-model="daten.bioGesch" class="form-check-input" type="radio" name="inputBioGesch" :id="aCheck.id" :value="aCheck.val">
						<label class="form-check-label" :for="aCheck.id">{{ aCheck.title }}</label>
					</div>
				</div>
			</div>
			<div class="form-group col-md-6">
				<label for="inputBeruf">Beruf</label>
				<input v-model="daten.beruf" type="text" class="form-control" id="inputBeruf" placeholder="Beruf">
			</div>
		</div>
		<div class="form-row">
			<div class="form-group col-md-6">
				<label for="inputWohnort">Aktueller Wohnort (inkl. Postleitzahl)</label>
				<div class="form-row">
					<div class="form-group col-sm-8 col-md-9"><input v-model="daten.wohnort.ort" type="text" class="form-control" id="inputWohnort" placeholder="Wohnort"></div>
					<div class="form-group col-sm-4 col-md-3"><input v-model="daten.wohnort.plz" type="number" class="form-control" id="inputWohnortPlz" placeholder="Postleitzahl"></div>
				</div>
			</div>
			<div class="form-group col-md-6">
				<label for="inputWohnortLeben">Wo haben Sie den Großteil Ihres Lebens verbracht? (inkl. Postleitzahl)</label>
				<div class="form-row">
					<div class="form-group col-sm-8 col-md-9"><input v-model="daten.wohnortLeben.ort" type="text" class="form-control" id="inputWohnortLeben" placeholder="Wohnort"></div>
					<div class="form-group col-sm-4 col-md-3"><input v-model="daten.wohnortLeben.plz" type="number" class="form-control" id="inputWohnortLebenPlz" placeholder="Postleitzahl"></div>
				</div>
			</div>
		</div>
		<div class="form-group">
			<label for="inputSprachenDialekte">Mit welchen Sprachen / Dialekten sind Sie aufgewachsen?</label>
			<input v-model="daten.sprachenDialekte" type="text" class="form-control" id="inputSprachenDialekte" placeholder="Sprachen, Dialekte">
		</div>

		<div class="alert alert-success" role="alert">
			<h4>Warum wollen wir das wissen?</h4>
			<p>Wir untersuchen, wie Menschen in Österreich Sprache verwenden, über Sprache denken und Sprache wahrnehmen. <b>Ihre Angaben helfen uns, Spracheinstellung in Österreich auszuwerten und besser zu verstehen.</b></p>
			<p><b>Weitere Angaben zu Ihnen</b> helfen uns Ihren Beitrag besonders gut in das Gesamtbild einzuordnen.</p>
		</div>
		<button @click="weitereAngaben = true" type="button" class="btn btn-success w-100" v-if="!weitereAngaben">Weitere Angaben machen</button>

		<div v-if="weitereAngaben">
			<br>
			<h4>Weitere Angaben: <button @click="weitereAngaben = false" type="button" class="btn btn-warning btn-sm float-right">Doch keine weitere Angaben machen</button></h4>
			<br>
			<p><b>Wo sind Ihre Eltern aufgewachsen?</b></p>
			<div class="form-row">
				<div class="form-group col-md-6">
					<label for="inputWohnortVater">Wohnort Vater (inkl. Postleitzahl)</label>
					<div class="form-row">
						<div class="form-group col-sm-8 col-md-9"><input v-model="daten.wohnortVater.ort" type="text" class="form-control" id="inputWohnortVater" placeholder="Wohnort"></div>
						<div class="form-group col-sm-4 col-md-3"><input v-model="daten.wohnortVater.plz" type="number" class="form-control" id="inputWohnortVaterPlz" placeholder="Postleitzahl"></div>
					</div>
				</div>
				<div class="form-group col-md-6">
					<label for="inputWohnortMutter">Wohnort Mutter (inkl. Postleitzahl)</label>
					<div class="form-row">
						<div class="form-group col-sm-8 col-md-9"><input v-model="daten.wohnortMutter.ort" type="text" class="form-control" id="inputWohnortMutter" placeholder="Wohnort"></div>
						<div class="form-group col-sm-4 col-md-3"><input v-model="daten.wohnortMutter.plz" type="number" class="form-control" id="inputWohnortMutterPlz" placeholder="Postleitzahl"></div>
					</div>
				</div>
			</div>
			<RadioFromTo v-model="daten.sprachlichErzogenVater" label="Wie wurden Sie von Ihrem Vater sprachlich erzogen? *" from="ausschließlich Dialekt" to="ausschließlich Hochdeutsch"/>
			<RadioFromTo v-model="daten.sprachlichErzogenMutter" label="Wie wurden Sie von Ihrem Mutter sprachlich erzogen? *" from="ausschließlich Dialekt" to="ausschließlich Hochdeutsch"/>
			<div class="form-row">
				<div class="form-group col-md-3">
					<label>Beherrschen Sie selbst einen Dialekt?</label>
					<div class="form-control">
						<div class="form-check form-check-inline">
							<input v-model="daten.dialektSelbst" class="form-check-input" type="radio" name="inputDialektSelbst" id="inputDialektSelbstJa" value="Ja">
							<label class="form-check-label" for="inputDialektSelbstJa">Ja</label>
						</div>
						<div class="form-check form-check-inline">
							<input v-model="daten.dialektSelbst" class="form-check-input" type="radio" name="inputDialektSelbst" id="inputDialektSelbstNein" value="Nein">
							<label class="form-check-label" for="inputDialektSelbstNein">Nein</label>
						</div>
					</div>
				</div>
				<div class="form-group col-md-9" v-if="daten.dialektSelbst === 'Ja'">
					<label for="inputDialektSelbstWelcher">Welchen Dialekt beherrschen Sie?</label>
					<input v-model="daten.dialektSelbstWelcher" type="text" class="form-control" id="inputDialektSelbstWelcher" placeholder="Dialekt">
				</div>
			</div>
			<RadioFromTo v-model="daten.dialektSprechen" label="Wie gut sprechen Sie diesen Dialekt?" from="gar nicht" to="sehr gut" v-if="daten.dialektSelbst === 'Ja'"/>
			<RadioFromTo v-model="daten.dialektNutzen" label="Wie häufig sprechen Sie Dialekt?" from="nie" to="immer" v-if="daten.dialektSelbst === 'Ja'"/>
			<RadioFromTo v-model="daten.hochdeutschSprechen" label="Wie gut sprechen Sie Hochdeutsch?" from="gar nicht" to="sehr gut"/>
			<RadioFromTo v-model="daten.hochdeutschNutzen" label="Wie häufig sprechen Sie Hochdeutsch?" from="nie" to="immer"/>
			<RadioFromTo v-model="daten.alltagSprechen" label="Wie sprechen Sie hauptsächlich in Ihrem Alltag?" from="ausschließlich Dialekt" to="ausschließlich Hochdeutsch"/>
			<div class="form-group" v-if="daten.alltagSprechen > 1 && daten.alltagSprechen < 7">
				<label for="inputBezeichnungSprechweise">Wie bezeichnen Sie diese Sprechweise, die Sie hauptsächlich in Ihrem Alltag sprechen?</label>
				<input v-model="daten.bezeichnungSprechweise" type="text" class="form-control" id="inputBezeichnungSprechweise" placeholder="">
			</div>
			<div class="form-group">
				<label for="inputAnmerkungen">Haben Sie noch Anmerkungen zu diesem Fragebogen?</label>
				<input v-model="daten.anmerkungen" type="text" class="form-control" id="inputAnmerkungen" placeholder="">
			</div>
		</div>

		<div class="alert alert-primary mt-3" role="alert">
			<h5 class="text-center">Der SFB „Deutsch in Österreich“ behandelt Ihre Daten vertraulich und ausschließlich für wissenschaftliche Zwecke.</h5>
		</div>
		<div class="form-group form-check">
			<input v-model="daten.dsgvo" type="checkbox" class="form-check-input" id="dsgvoCheck">
			<label class="form-check-label" for="dsgvoCheck">Ich erkläre mich damit einverstanden, dass meine personenbezogenen Daten - wie in der <a href="https://iam.dioe.at/datenschutz/" target="_blank">Datenschutzerklärung</a> beschrieben - vom SFB „Deutsch in Österreich: Variation – Kontakt – Perzeption“ wissenschaftlich ausgewertet werden und im Zuge dessen innerhalb des SFBs verwendet werden. Diese Einwilligung kann ich jederzeit widerrufen.</label>
		</div>

		<button @click="" type="button" class="btn btn-primary w-100" :disabled="!daten.dsgvo">Los geht’s</button>

	</div>
</template>

<script>
import RadioFromTo from './formular/RadioFromTo'

export default {
	name: 'DataPage',
	data () {
		return {
			weitereAngaben: false,
			daten: {
				geburtsjahr: '',
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
		}
	},
	components: {
		RadioFromTo,
	},
}
</script>

<style scoped>
</style>
