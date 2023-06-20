<template>
  <section class="bk-layout-custom-component-wrapper container-dlomhlhb">
    <div class="bk-layout-component-dlomhlhb block3ed1c"></div>

    <div class="bk-free-layout-dlomhlhb free-layout-15f10">
      <div style="position: absolute; top: 183px; left: 34px; width: 547px;">
        <bk-steps
          :steps="stepsF05ebsteps"
          :cur-step="1"
          direction="horizontal"
          theme="primary"
          :controllable="false"
          class="bk-layout-component-dlomhlhb stepsF05eb"></bk-steps>
      </div>
      <div absolute-align-horizontal-right style="position: absolute; top: 169px; left: 33px; width: 1189px;">
        <bk-progress
          theme="primary"
          :percent="0.5"
          size="normal"
          :text-inside="false"
          :show-text="true"
          :title-style="progress7232etitleStyle"
          class="bk-layout-component-dlomhlhb progress7232e"></bk-progress>
      </div>
      <div style="position: absolute; top: 77px; left: 50px; width: 58px;">
        <span title="" class="bk-layout-component-dlomhlhb text47f96"> 物品质量</span>
      </div>
      <div style="position: absolute; top: 29px; left: 50px; width: 58px;">
        <span title="" class="bk-layout-component-dlomhlhb text79c74"> 背包容量</span>
      </div>
      <div style="position: absolute; top: 277px; left: 12px; width: 87px;">
        <span title="" class="bk-layout-component-dlomhlhb textE0e1a"> 背包容量范围</span>
      </div>
      <div style="position: absolute; top: 345px; left: 10px; width: 87px;">
        <span title="" class="bk-layout-component-dlomhlhb text2ae5a"> 物品质量范围</span>
      </div>
      <div style="position: absolute; top: 273px; left: 958px; width: 87px;">
        <span title="" class="bk-layout-component-dlomhlhb textAed91"> 测试次数</span>
      </div>
      <div style="position: absolute; top: 77px; left: 422px; width: 58px;">
        <span title="" class="bk-layout-component-dlomhlhb text3e36a"> 物品价值</span>
      </div>
      <div style="position: absolute; top: 349px; left: 386px; width: 88px;">
        <span title="" class="bk-layout-component-dlomhlhb text5b242"> 物品价值范围</span>
      </div>
      <div style="position: absolute; top: 33px; left: 423px; width: 58px;">
        <span title="" class="bk-layout-component-dlomhlhb textE6f8b"> 物品数目</span>
      </div>
      <div style="position: absolute; top: 281px; left: 389px; width: 85px;">
        <span title="" class="bk-layout-component-dlomhlhb text208b7"> 物品数目范围</span>
      </div>
      <div style="position: absolute; top: 25px; left: 119px; width: 100px;">
        <bk-input
          v-model="capacity"
          value=""
          type="number"
          font-size="normal"
          :max="200"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb inputEb760"></bk-input>
      </div>
      <div style="position: absolute; top: 310px; left: 851px; width: 300px;">
        <bk-input
          v-model="testNumber"
          value=""
          type="number"
          font-size="normal"
          :max="10000"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input5f1a5"></bk-input>
      </div>
      <div style="position: absolute; top: 343px; left: 622px; width: 120px;">
        <bk-input
          v-model="valueMax"
          value=""
          type="number"
          font-size="normal"
          :max="100"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input2a062"></bk-input>
      </div>
      <div style="position: absolute; top: 344px; left: 483px; width: 120px;">
        <bk-input
          v-model="valueMin"
          value=""
          type="number"
          font-size="normal"
          :max="100"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input7636e"></bk-input>
      </div>
      <div style="position: absolute; top: 342px; left: 233px; width: 120px;">
        <bk-input
          v-model="weightMax"
          value=""
          type="number"
          font-size="normal"
          :max="100"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input1581e"></bk-input>
      </div>
      <div style="position: absolute; top: 275px; left: 100px; width: 120px;">
        <bk-input
          v-model="capacityMin"
          value=""
          type="number"
          font-size="normal"
          :max="200"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb inputC9877"></bk-input>
      </div>
      <div style="position: absolute; top: 276px; left: 230px; width: 120px;">
        <bk-input
          v-model="capacityMax"
          value=""
          type="number"
          font-size="normal"
          :max="200"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb inputA936e"></bk-input>
      </div>
      <div style="position: absolute; top: 341px; left: 101px; width: 120px;">
        <bk-input
          v-model="weightMin"
          value=""
          type="number"
          font-size="normal"
          :max="200"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input8793f"></bk-input>
      </div>
      <div style="position: absolute; top: 277px; left: 622px; width: 120px;">
        <bk-input
          v-model="numberMax"
          value=""
          type="number"
          font-size="normal"
          :max="50"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb inputC33b3"></bk-input>
      </div>
      <div style="position: absolute; top: 277px; left: 482px; width: 120px;">
        <bk-input
          v-model="numberMin"
          value=""
          type="number"
          font-size="normal"
          :max="50"
          :min="1"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb inputD1143"></bk-input>
      </div>
      <div style="position: absolute; top: 72px; left: 119px; width: 220px;">
        <bk-input
          v-model="weight"
          value=""
          type="text"
          font-size="normal"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input91e66"></bk-input>
      </div>
      <div style="position: absolute; top: 72px; left: 852px; width: 300px;">
        <bk-input
          v-model="result"
          value=""
          type="number"
          font-size="normal"
          :max="10000000"
          :min="0"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input757c4"></bk-input>
      </div>
      <div absolute-align-horizontal-right style="position: absolute; top: 454px; margin-top: 0px; width: 500px;">
        <bk-input
          v-model="testResult"
          value=""
          type="text"
          font-size="normal"
          :max="10000000"
          :min="0"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input31f80"></bk-input>
      </div>
      <div style="position: absolute; top: 72px; left: 499px; width: 220px;">
        <bk-input
          v-model="value"
          value=""
          type="text"
          font-size="normal"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb inputA099a"></bk-input>
      </div>
      <div style="position: absolute; top: 26px; left: 499px; width: 135px;">
        <bk-input
          v-model="number"
          value=""
          type="number"
          :max="50"
          :min="1"
          font-size="normal"
          :disabled="false"
          :readonly="false"
          :clearable="true"
          :show-controls="true"
          class="bk-layout-component-dlomhlhb input4ecb8"></bk-input>
      </div>
      <div style="position: absolute; top: 24px; left: 948px;">
        <bk-button
          title="hello world"
          size="normal"
          theme="primary"
          :disabled="false"
          :loading="false"
          icon="bk-icon icon-arrows-down-shape"
          @click="caculate"
          class="bk-layout-component-dlomhlhb button48c34">
          计算结果
        </bk-button>
      </div>
      <div style="position: absolute; top: 410px; left: 951px;">
        <bk-button
          title="hello world"
          size="normal"
          theme="primary"
          :disabled="false"
          :loading="false"
          icon="bk-icon icon-arrows-down-shape"
          @click="testCaculate"
          class="bk-layout-component-dlomhlhb buttonFe5c8">
          运行情况
        </bk-button>
      </div>
    </div>
  </section>
</template>

<script>
import {bkFormItem, bkForm, bkButton, bkInput, bkSteps, bkProgress} from 'bk-magic-vue'
import axios from 'axios'
import {host} from '../../static/js/host'


export default {
  name: 'dp',
  components: {
    bkFormItem,
    bkForm,
    bkButton,
    bkInput,
    bkSteps,
    bkProgress
  },
  data() {
    return {
      testNumber: 1,
      capacityMax: 1,
      capacityMin: 1,
      capacity: 1,
      valueMax: 1,
      valueMin: 1,
      value: "",
      numberMax: 1,
      numberMin: 1,
      number: 1,
      weightMax: 1,
      weightMin: 1,
      weight: "",
      result: 0,
      testResult: "",
      stepsF05ebsteps: [
        {title: '步骤1', icon: 1, description: ''},
        {title: '步骤2', icon: 2, description: ''}
      ],
      progress7232etitleStyle: {fontSize: '16px', verticalAlign: 'middle'}
    }
  },
  methods: {
    caculate() {
      axios.post(host + '/caculate/dp/', JSON.parse(JSON.stringify(
        {
          'capacity': this.capacity,
          'value': this.value,
          'number': this.number,
          'weight': this.weight
        })), {
        responseType: 'json'
      }).then(response => {
        this.handlePrimarySuccess()
        alert(response.data.res)
        this.result = response.data.res
      })
        .catch(error => {
          this.handlePrimaryFail()
          alert(error.response.data.message)
          console.log(error.response.data)
        })
    },
    testCaculate() {
      axios.post(host + '/caculate_test/dp/', JSON.parse(JSON.stringify(
        {
          'testNumber': this.testNumber,
          'capacityMax': this.capacityMax,
          'capacityMin': this.capacityMin,
          'valueMax': this.valueMax,
          'valueMin': this.valueMin,
          'numberMax': this.numberMax,
          'numberMin': this.numberMin,
          'weightMax': this.weightMax,
          'weightMin': this.weightMin
        })), {
        responseType: 'json'
      }).then(response => {
        this.handlePrimarySuccess()
        this.testResult = response.data.res
      })
        .catch(error => {
          this.handlePrimaryFail()
          alert(error.response.data.message)
          console.log(error.response.data)
        })
    },
    handlePrimarySuccess() {
      var config = {theme: 'success'}
      config.message = "计算成功"
      config.offsetY = 80
      this.$bkMessage(config)
    },
    handlePrimaryFail() {
      var config = {theme: 'error'}
      config.message = "运行失败"
      config.offsetY = 80
      this.$bkMessage(config)
    },
  }
}
</script>

<style lang="css" scoped>
.container-dlomhlhb {
  padding-left: 24px;
  padding-right: 24px;
  padding-top: 20px;
  padding-bottom: 0px;
  height: 100%;
}

.bk-layout-row-dlomhlhb {
  display: flex;
}

.bk-layout-row-dlomhlhb:after {
  display: block;
  clear: both;
  content: '';
  font-size: 0;
  height: 0;
  visibility: hidden;
}

.bk-layout-col-dlomhlhb {
  float: left;
  position: relative;
  min-height: 1px;
}

.bk-free-layout-dlomhlhb {
  height: 500px;
  width: 100%;
  display: inline-block;
  position: relative;
}

.bk-free-layout-item-inner-dlomhlhb {
  height: 100%;
  position: relative;
}

.bk-form-radio {
  margin-right: 20px;
}

.bk-form-checkbox {
  margin-right: 20px;
}

.echarts {
  width: 100%;
  height: 100%;
}

/* 设置 bk-exception 组件宽度为 100% */
.bk-exception-img {
  width: 100%;
}

.bk-form-item {
  margin: 10px;
}

.bk-sideslider {
  margin: 0;
}

/* 设置 .bk-form-control 组件宽度为 auto */
.bk-form-control {
  width: auto;
}

.bk-form-control .bk-input-text {
  font-size: 12px;
}

[align-horizontal-left] > *,
[align-horizontal-center] > *,
[align-horizontal-right] > *,
[align-horizontal-space-between] > *,
[align-vertical-top] > *,
[align-vertical-center] > *,
[align-vertical-bottom] > * {
  flex-shrink: 0;
}

[align-horizontal-left],
[align-horizontal-center],
[align-horizontal-right],
[align-horizontal-space-between] {
  display: flex !important;
  align-items: flex-start;
  flex-wrap: wrap;
}

[align-horizontal-left] {
  justify-content: flex-start;
}

[align-horizontal-center] {
  justify-content: center;
}

[align-horizontal-right] {
  justify-content: flex-end;
}

[align-horizontal-space-between] {
  justify-content: space-between;
}

[align-vertical-top],
[align-vertical-center],
[align-vertical-bottom] {
  display: flex !important;
  flex-wrap: wrap;
}

[align-vertical-top] {
  align-items: flex-start;
}

[align-vertical-center] {
  align-items: center;
}

[align-vertical-bottom] {
  align-items: flex-end;
}

[absolute-align-horizontal-left] {
  left: 0 !important;
}

[absolute-align-horizontal-center] {
  left: 50% !important;
  transform: translateX(-50%) !important;
}

[absolute-align-horizontal-right] {
  left: unset !important;
  right: 0 !important;
}

[absolute-align-vertical-top] {
  top: 0 !important;
}

[absolute-align-vertical-center] {
  top: 50% !important;
  transform: translateY(-50%) !important;
}

[absolute-align-vertical-bottom] {
  top: unset !important;
  bottom: 0 !important;
}

[absolute-align-horizontal-center][absolute-align-vertical-center] {
  transform: translate(-50%, -50%) !important;
}

.bk-layout-component-dlomhlhb.block3ed1c {
  display: block;
  width: 100%;
}

.free-layout-15f10 {
  height: 490px;
  margin-top: 8px;
  width: 1224px;
}

.bk-layout-component-dlomhlhb.stepsF05eb {
  width: 547px;
}

.bk-layout-component-dlomhlhb.progress7232e {
  width: 1189px;
}

.bk-layout-component-dlomhlhb.text47f96 {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 58px;
}

.bk-layout-component-dlomhlhb.text79c74 {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 58px;
}

.bk-layout-component-dlomhlhb.textE0e1a {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 87px;
}

.bk-layout-component-dlomhlhb.text2ae5a {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 87px;
}

.bk-layout-component-dlomhlhb.textAed91 {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 87px;
}

.bk-layout-component-dlomhlhb.text3e36a {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 58px;
}

.bk-layout-component-dlomhlhb.text5b242 {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 88px;
}

.bk-layout-component-dlomhlhb.textE6f8b {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 58px;
}

.bk-layout-component-dlomhlhb.text208b7 {
  display: inline-block;
  text-align: center;
  font-size: 14px;
  vertical-align: middle;
  width: 85px;
}

.bk-layout-component-dlomhlhb.inputEb760 {
  display: inline-block;
  vertical-align: middle;
  width: 100px;
}

.bk-layout-component-dlomhlhb.input5f1a5 {
  display: inline-block;
  vertical-align: middle;
  width: 300px;
}

.bk-layout-component-dlomhlhb.input2a062 {
  display: inline-block;
  vertical-align: middle;
  width: 120px;
}

.bk-layout-component-dlomhlhb.input7636e {
  display: inline-block;
  vertical-align: middle;
  width: 120px;
}

.bk-layout-component-dlomhlhb.input1581e {
  display: inline-block;
  vertical-align: middle;
  width: 120px;
}

.bk-layout-component-dlomhlhb.inputC9877 {
  display: inline-block;
  vertical-align: middle;
  width: 120px;
}

.bk-layout-component-dlomhlhb.inputA936e {
  display: inline-block;
  vertical-align: middle;
  width: 120px;
}

.bk-layout-component-dlomhlhb.input8793f {
  display: inline-block;
  vertical-align: middle;
  width: 120px;
}

.bk-layout-component-dlomhlhb.inputC33b3 {
  display: inline-block;
  vertical-align: middle;
  width: 120px;
}

.bk-layout-component-dlomhlhb.inputD1143 {
  display: inline-block;
  vertical-align: middle;
  width: 120px;
}

.bk-layout-component-dlomhlhb.input91e66 {
  display: inline-block;
  vertical-align: middle;
  width: 220px;
}

.bk-layout-component-dlomhlhb.input757c4 {
  display: inline-block;
  vertical-align: middle;
  width: 300px;
}

.bk-layout-component-dlomhlhb.input31f80 {
  display: inline-block;
  vertical-align: middle;
  width: 500px;
  min-width: 1px;
}

.bk-layout-component-dlomhlhb.inputA099a {
  display: inline-block;
  vertical-align: middle;
  width: 220px;
}

.bk-layout-component-dlomhlhb.input4ecb8 {
  display: inline-block;
  vertical-align: middle;
  width: 135px;
}

.bk-layout-component-dlomhlhb.button48c34 {
  display: inline-block;
  vertical-align: middle;
}

.bk-layout-component-dlomhlhb.buttonFe5c8 {
  display: inline-block;
  vertical-align: middle;
}
</style>
