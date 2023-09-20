<script>
export default {
  data() {
    return {
      modbusStatus: "連線中...",
      isLoading: true,
      isConnected: false,
    };
  },
  mounted() {
    eel.modbus_status()((status) => {
      this.modbusStatus = status ? "連線成功 !!!" : "連線失敗 !!!";
      this.isLoading = false;
    });
  },
};
</script>

<template>
  <div id="page1" class="section">
    <h1 id="modbus_status" v-text="modbusStatus"></h1>
    <div v-if="isLoading">
      <img
        src="../img/loading_icon.gif"
        alt="連線中..."
        id="modbus_status_icon"
      />
    </div>

    <div>
      <h1 id="subtitle">測量顯示</h1>
      <table class="table table-light mb-0">
        <thead style="background-color: #393939">
          <tr class="text-uppercase text-success">
            <th></th>
            <th scope="col">項目</th>
            <th scope="col">目標值</th>
            <th scope="col">實測值</th>
            <th scope="col">判定值</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td></td>
            <td>端面角度</td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
          </tr>
          <tr>
            <td></td>
            <td>端面寬度</td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
          </tr>
          <tr>
            <td></td>
            <td>直角度</td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
          </tr>
          <tr class="text-uppercase text-success">
            <td></td>
            <td></td>
            <th scope="col">目標值</th>
            <th scope="col">Count</th>
            <th scope="col">NG數</th>
          </tr>
          <tr>
            <td></td>
            <td>生產Count</td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
          </tr>
          <tr>
            <td></td>
            <td>Cycle Time</td>
            <td>
              <div class="col-4">
                <input type="text" class="form-control" disabled />
              </div>
            </td>
            <td></td>
            <td></td>
          </tr>
        </tbody>
      </table>
      <button id="submitBtn" type="button" class="btn btn-primary btn-lg">
        送出
      </button>
    </div>
  </div>
</template>
