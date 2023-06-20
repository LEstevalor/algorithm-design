<template>
  <div style="background-color: #f5ece7">
    <bk-process
      :list="list"
      :cur-process.sync="process"
      :display-key="'content'"
      @process-changed="change"
      :controllable="true"></bk-process>
    <br/>
    <p>
      <bk-button theme="primary" @click="handleSingle({position: placement.topRight, theme:'primary'})">
        Welcome to use algorithm test platform
      </bk-button>
    </p>
    <br/><br/><br/><br/><br/><br/><br/>
    <fx67ll-binary-clock :isShowTime="true" :zoomSize="1"></fx67ll-binary-clock>
  </div>
</template>

<script>
// import { bkSwiper } from 'bk-magic-vue'
import {bkProcess, bkButton} from 'bk-magic-vue'

export default {
  name: 'top',
  components: {
    // bkSwiper // 轮播图
    bkProcess,
    bkButton
  },
  data() {
    return {
      process: 1,
      list: [
        {
          content: '进入首页'
        },
        {
          content: '选择算法'
        },
        {
          content: '输入样例'
        },
        {
          content: '得到结果'
        },
        {
          content: '集中测试'
        }
      ],
      title: '你好！欢迎你使用GDUT算法实验平台',
      message: '目前免登录测试01背包问题，可选用DP、贪心、回溯、优化DP方法，后续算法与模型待开发中。。。',
      placement: {
        topRight: 'top-right'
      }
    }
  },
  methods: {
    change (process, data) {
      alert('当前process:' + process)
      console.log(process)
      console.log(data)
    },
    handleSingle (config) {
      config.title = this.title
      config.message = this.message
      config.offsetY = 200
      config.limitLine = 15
      this.$bkNotify(config)
    }
  }
}
</script>

<style scoped>

</style>
