import './assets/style.css';
import dataurl from './assets/sample_summary_data.json';

const grid = 500;
var itr = 1;

async function addSticky() {

    dataurl.themes.map(async (e) => {
        e.urls.map(async (url) => {
            var todo = await miro.board.createStickyNote({
                content: url,
                x: itr * grid,
                y: grid + 100,
            })
            itr++;
        })
        
        var card = await miro.board.createCard({
            title: e.name,
            x: itr * grid,
            y: grid,
        }); 

        await miro.board.viewport.zoomTo(card);
    })

    
    
}

addSticky(); 
