<%inherit file="main.mak"/>
<div class="row uninett-color-white uninett-whole-row uninett-padded">
  <h2>NREC via Dataporten</h2>
  <br/>
% if was_provisioned:
  <h3>Reset API password</h3>
  <p>Username: '${api_user_name}'
  <br/>
  Password: '${api_pw}'</p>
  <p>NB! Remember to write the password down for later use.</p>
  <a href="${dashboard_url}" class="btn btn-default uninett-login-btn">
    <span class="glyphicon glyphicon-user uninett-fontColor-red"></span>
    Continue to NREC
  </a>
%else:
  <p>You have not signed up to NREC yet.</p>
  <p>Before signing up to NREC, make sure that you have read and understood our
  <a href="http://docs.nrec.no/en/latest/terms-of-service.html" target="blank">
  Terms of Service</a>.</p><br/>
  <a href="/login" class="btn btn-default uninett-login-btn">
    <span class="glyphicon glyphicon-user uninett-fontColor-red"></span>
    Sign up
  </a><br>
% endif
  <br/>
  <p>You may be sent back to Dataporten again.</p>
</div>
