<template>
  <div id="page3" class="section">
    <h1 id="subtitle">測量設定</h1>
    <table class="table table-light mb-0">
      <thead style="background-color: #393939">
        <tr class="text-uppercase text-success">
          <th></th>
          <th scope="col">生產NO.</th>
          <th scope="col">鋼管直徑</th>
          <th scope="col">鋼管長度</th>
          <th scope="col">鋼管厚度</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td></td>
          <td>
            <div class="col-4">
              <input type="text" class="form-control" />
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
          <td>
            <div class="col-4">
              <input type="text" class="form-control" disabled />
            </div>
          </td>
        </tr>
      </tbody>
      <tr class="text-uppercase text-success">
        <th></th>
        <th scope="col">項目</th>
        <th scope="col">目標值</th>
        <th scope="col">max容許值</th>
        <th scope="col">min容許值</th>
      </tr>
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
              <input type="text" class="form-control" />
            </div>
          </td>
          <td>
            <div class="col-4">
              <input type="text" class="form-control" />
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
              <input type="text" class="form-control" />
            </div>
          </td>
          <td>
            <div class="col-4">
              <input type="text" class="form-control" />
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
              <input type="text" class="form-control" />
            </div>
          </td>
          <td>
            <div class="col-4">
              <input type="text" class="form-control" />
            </div>
          </td>
        </tr>
        <tr>
          <td></td>
          <td>生產數量</td>
          <td>
            <div class="col-4">
              <input type="text" class="form-control" />
            </div>
          </td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table>
    <button id="submitBtn" type="button" class="btn btn-primary btn-lg">
      Submit
    </button>
  </div>
</template>
