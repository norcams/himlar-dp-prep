<%inherit file="main.mak"/>
<div class="row uninett-color-white uninett-whole-row uninett-padded">
  <h2>${header}</h2>
  <p>${message}</p>
% if provisioned:
 <p>Continue to NREC <a href="${dashboard_url}">[her].</a></p>
%else:
  <p>You have not signed up to NREC yet.</p>
  <p>Before signing up to NREC, make sure that you have read and understood our
  <a href="http://docs.nrec.no/en/latest/terms-of-service.html" target="blank">
  Terms of Service</a>.</p>
% endif
 <p>You may be sent back to Dataporten again.</p>
</div>
