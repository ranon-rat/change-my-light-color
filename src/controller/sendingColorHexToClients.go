package controller

import (
	"time"

	"github.com/gofiber/websocket/v2"
)

func SendColorHex(ctx *websocket.Conn) {

	for {
		color := <-colorChan
		if err := ctx.WriteMessage(websocket.TextMessage, color); err != nil {
			return
		}
		time.Sleep(time.Second * 2)
	}

}
