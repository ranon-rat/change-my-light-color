package controller

import "github.com/gofiber/fiber/v2"

var (
	colorChan = make(chan []byte)
)

func ReceiveColorHex(ctx *fiber.Ctx) error {
	colorChan <- (ctx.Request().Body())

	return ctx.SendString("¡you should love yourself now!")
}
