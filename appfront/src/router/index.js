import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/', // 公有模板页
      name: 'index',
      component: () => import('../components/index.vue'),
      children: [
        {
          path: '/top', // 要跟在父路径的路径后，/father/child
          name: 'index.top', // 名称也是
          component: () => import('../components/top.vue')
        },
        {
          path: '/dp',
          name: 'index.dp',
          component: () => import('../components/dp.vue')
        },
        {
          path: '/greedy',
          name: 'index.greedy',
          component: () => import('../components/greedy.vue')
        },
        {
          path: '/backtrack',
          name: 'index.backtrack',
          component: () => import('../components/backtrack.vue')
        },
        {
          path: '/dpplus',
          name: 'index.dpplus',
          component: () => import('../components/dpplus.vue')
        },
        // {
        //   path: '/testone',
        //   name: 'index.testone',
        //   component: () => import('../components/testone.vue')
        // },
      ]
    }
  ]
})
