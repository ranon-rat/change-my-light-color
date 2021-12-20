package router

import (
	"os"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/websocket/v2"
	"github.com/ranon-rat/change-my-light-color/src/controller"
)

func SetupRouter() {
	app := fiber.New()
	port := os.Getenv("PORT")
	app.Static("/", "./static")
	app.Post("/color", controller.ReceiveColorHex)
	app.Use("/color", func(c *fiber.Ctx) error {

		if websocket.IsWebSocketUpgrade(c) {
			c.Locals("allowed", true)
			return c.Next()
		}
		return fiber.ErrUpgradeRequired
	})
	app.Get("/color", websocket.New(controller.SendColorHex))
	if port == "" {
		port = "8080"
	}
	app.Listen(":" + port)
}
