var store_items_json = require('./golive/data/store_items.json');
var store_items = store_items_json["store_items"];
var offer_classification_json = require('./golive/data/offer_classification.json');
var offer_classification = offer_classification_json["Offers"];
var create_offers = require('./create_offers.js');
var fs = require('fs');

var classified_users = new Array();
var users_with_offers = new Object();
users_with_offers["Users_and_offers"] = new Array();
for(var offer of offer_classification)
{
    var classification = require('./golive/output/classified_users/classification_' + String(offer.offer_id) + '.json');
    var user_offer = create_offers.generateOffer(store_items, offer.offer_price, new Set(offer.offer_type), offer.multiple);
    let array = Array.from(user_offer);
    classification["generated_offer"] = array;
    users_with_offers["Users_and_offers"].push(classification);
    //fs.writeFileSync('./golive/output/classified_users/classification_' + String(offer.offer_id) + '.json', JSON.stringify(classification, null, 4));
}
fs.writeFileSync('./golive/output/final_output/output.json', JSON.stringify(users_with_offers, null, 4));
